#!/usr/bin/env python3
"""
Fix files in this repo that differ only in letter case (Kor.md and kor.md).

macOS and Windows can't hold both on disk, so Git keeps showing one of them
as modified and pulling or pushing gets stuck. It happens when a note gets
renamed by changing only a capital. For every such group, the path that was
changed most recently is kept and the others are removed. The fix is pushed
and the files on disk are brought in line with it.

Usage: python3 fix-case-duplicates.py [--dry-run]
"""
import argparse
import os
import subprocess
import sys
import tempfile

REMOTE = "origin"
PUSH_ATTEMPTS = 3

def abort_stuck_operations():
    git_dir = git("rev-parse", "--git-dir").strip()

    if any(os.path.isdir(os.path.join(git_dir, name)) for name in ("rebase-merge", "rebase-apply")):
        print("Aborting a rebase that got stuck")
        git("rebase", "--abort")

    if os.path.exists(os.path.join(git_dir, "MERGE_HEAD")):
        print("Aborting a merge that got stuck")
        git("merge", "--abort")

def case_groups(commit: str) -> list[list[str]]:
    groups = {}

    for path in split_nul(git("ls-tree", "-r", "-z", "--name-only", commit)):
        groups.setdefault(path.casefold(), []).append(path)

    return [sorted(paths) for paths in groups.values() if len(paths) > 1]

def combined_commit(head: str, upstream: str) -> str:
    if is_ancestor(head, upstream):
        return upstream

    if is_ancestor(upstream, head):
        return head

    # Both sides have new commits: merge them without touching the files on disk
    result = subprocess.run(
        ["git", "merge-tree", "--write-tree", "--name-only", head, upstream],
        capture_output = True,
        text = True
    )

    if result.returncode != 0:
        fail(
            "Your commits and the ones on GitHub change the same lines:\n"
            f"{result.stdout.strip()}\n"
            "Merge these by hand first, then run this script again."
        )

    tree = result.stdout.splitlines()[0]
    return git("commit-tree", tree, "-p", head, "-p", upstream, "-m", "Merge changes from GitHub").strip()

def fail(message: str):
    print(f"\n{message}", file = sys.stderr)
    sys.exit(1)

def fix_commit(base: str) -> tuple[str, list[tuple[str, list[str]]]]:
    fixes = []

    for paths in case_groups(base):
        keep = max(paths, key = lambda path: last_change(base, path))
        fixes.append((keep, [path for path in paths if path != keep]))

    if not fixes:
        return base, fixes

    with tempfile.TemporaryDirectory() as tmp:
        env = {
            **os.environ,
            "GIT_INDEX_FILE" : os.path.join(tmp, "index")
        }
        git("read-tree", base, env = env)
        removed = [path for _, paths in fixes for path in paths]
        git("update-index", "--force-remove", "-z", "--stdin", env = env, stdin = "\0".join(removed) + "\0")
        tree = git("write-tree", env = env).strip()

    message = "Remove files that differ only in letter case\n\n" + "\n".join(
        f"Kept {keep}, removed {', '.join(removed)}" for keep, removed in fixes
    )
    return git("commit-tree", tree, "-p", base, "-m", message).strip(), fixes

def git(*args, env = None, stdin = None, check = True) -> str:
    result = subprocess.run(
        ["git", "--literal-pathspecs", *args],
        capture_output = True,
        env = env,
        input = stdin,
        text = True
    )

    if check and result.returncode != 0:
        fail(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")

    return result.stdout

def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", ancestor, descendant]).returncode == 0

def last_change(commit: str, path: str) -> int:
    # Match the path exactly, also on case-insensitive systems
    timestamp = git("-c", "core.ignorecase=false", "log", "-1", "--format=%ct", commit, "--", path).strip()
    return int(timestamp or 0)

def local_changes() -> list[tuple[str, str]]:
    entries = split_nul(git("status", "--porcelain=v1", "-z", "--no-renames", "--untracked-files=all"))
    return [(entry[:2], entry[3:]) for entry in entries]

def main():
    parser = argparse.ArgumentParser(description = "Fix files that differ only in letter case")
    parser.add_argument("--dry-run", action = "store_true", help = "only show what would happen")
    args = parser.parse_args()

    os.chdir(git("rev-parse", "--show-toplevel").strip())

    if not args.dry_run:
        abort_stuck_operations()

    branch = git("symbolic-ref", "--short", "HEAD", check = False).strip()

    if not branch:
        fail("You're not on a branch, so I don't know what to fix.")

    for attempt in range(PUSH_ATTEMPTS):
        print(f"Fetching from {REMOTE}")
        git("fetch", "-q", REMOTE)
        head = git("rev-parse", "HEAD").strip()
        upstream = git("rev-parse", f"{REMOTE}/{branch}").strip()
        base = combined_commit(head, upstream)
        target, fixes = fix_commit(base)
        stale = stale_paths(head, upstream, target)

        report(fixes, stale)

        if args.dry_run:
            print("\nDry run, nothing changed")
            return

        if target == head == upstream and not stale:
            print("\nNothing to fix")
            return

        if target != upstream:
            print(f"\nPushing to {REMOTE}/{branch}")
            pushed = subprocess.run(
                ["git", "push", "-q", REMOTE, f"{target}:refs/heads/{branch}"],
                capture_output = True,
                text = True
            )

            if pushed.returncode != 0:
                print("Push was refused, probably someone pushed in the meantime. Trying again.")
                continue

        sync_worktree(head, target, stale)
        print("\nDone: everything is pushed and the files on disk match")
        return

    fail(f"Pushing failed {PUSH_ATTEMPTS} times, try again in a minute.")

def report(fixes: list[tuple[str, list[str]]], stale: set[str]):
    if not fixes:
        print("No files that differ only in letter case")

    for keep, removed in fixes:
        print(f"\nKeeping   {keep}")

        for path in removed:
            print(f"Removing  {path}")

    if stale:
        print(f"\n{len(stale)} file(s) on disk will be replaced with the version from Git")

def split_nul(output: str) -> list[str]:
    return [item for item in output.split("\0") if item]

def stale_paths(head: str, upstream: str, target: str) -> set[str]:
    """
    Find files that have to be rewritten on disk: everything that changes
    between HEAD and the target commit, plus every case duplicate.
    """
    duplicates = {path for commit in (head, upstream) for paths in case_groups(commit) for path in paths}
    folded_duplicates = {path.casefold() for path in duplicates}
    changed = set(split_nul(git("diff", "--no-renames", "--name-only", "-z", head, target)))
    paths = changed | duplicates

    # Local changes are only allowed on duplicates: those are the phantom
    # modifications this script exists to clear up
    folded_paths = {path.casefold() for path in paths}
    blocking = []

    for status, path in local_changes():
        if status == "??":
            if path.casefold() in folded_paths:
                blocking.append(path)
        elif path.casefold() in folded_duplicates:
            paths.add(path)
        else:
            blocking.append(path)

    if blocking:
        fail(
            "These files have changes that aren't committed yet:\n"
            + "\n".join(f"  {path}" for path in blocking)
            + "\nCommit them (or let Obsidian do it) and run this script again."
        )

    if head == target and not any(path.casefold() in folded_duplicates for _, path in local_changes()):
        return set()

    return paths

def sync_worktree(head: str, target: str, paths: set[str]):
    git("reset", "-q", "--mixed", target)

    # On a case-insensitive disk this also removes the file under its other spelling
    for path in paths:
        if os.path.lexists(path):
            os.remove(path)

    target_paths = set(split_nul(git("ls-tree", "-r", "-z", "--name-only", target)))
    restore = sorted(paths & target_paths)

    if restore:
        git("checkout", "--pathspec-from-file=-", "--pathspec-file-nul", stdin = "\0".join(restore) + "\0")

if __name__ == "__main__":
    main()