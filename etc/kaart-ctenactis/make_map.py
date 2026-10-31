import json, sys
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
LON=(104,136); LAT=(-11,7)
land=json.load(open(sys.argv[1]))
polys=[]
for f in land["features"]:
    g=f["geometry"]; parts=g["coordinates"] if g["type"]=="MultiPolygon" else [g["coordinates"]]
    for p in parts:
        ring=p[0]
        xs=[c[0] for c in ring]; ys=[c[1] for c in ring]
        if max(xs)<LON[0]-2 or min(xs)>LON[1]+2 or max(ys)<LAT[0]-2 or min(ys)>LAT[1]+2: continue
        polys.append(Polygon(ring,closed=True))
rows=[r.split(",") for r in open(sys.argv[2]).read().strip().split(";")]
obs=[(float(a),float(b)) for a,b,y,t in rows if t in("I","O")]
spc=[(float(a),float(b)) for a,b,y,t in rows if t=="S"]
inbox=lambda p: LAT[0]<=p[0]<=LAT[1] and LON[0]<=p[1]<=LON[1]
obs=[p for p in obs if inbox(p)]; spc=[p for p in spc if inbox(p)]
SURF="#fcfcfb"; SEA="#eef3f6"; LAND="#d9d7d0"; T1="#0b0b0b"; T2="#52514e"
fig,ax=plt.subplots(figsize=(10,6.2),dpi=150)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SEA)
ax.add_collection(PatchCollection(polys,facecolor=LAND,edgecolor="#bdbab2",linewidth=0.3,zorder=1))
ax.scatter([p[1] for p in obs],[p[0] for p in obs],s=34,c="#2a78d6",edgecolors=SURF,linewidths=1.2,zorder=3,label=f"Waarnemingen 2000–2026 (vooral iNaturalist), {len(obs)} in dit kaartbeeld")
ax.scatter([p[1] for p in spc],[p[0] for p in spc],s=40,marker="s",c="#1baf7a",edgecolors=SURF,linewidths=1.2,zorder=4,label=f"Museumexemplaren 1980–1986, {len(spc)} in dit kaartbeeld")
sel=(120.46,-6.12)
ax.scatter([sel[0]],[sel[1]],s=260,marker="*",c="#eb6834",edgecolors=SURF,linewidths=1.5,zorder=5,label="Siboga-expeditie, 26 september 1899 (Selayar, plek bij benadering)")
ax.annotate("Siboga 1899\nSelayar",xy=sel,xytext=(sel[0]+1.2,sel[1]-2.3),fontsize=9,color=T1,arrowprops=dict(arrowstyle="-",color=T2,lw=0.8),zorder=6)
ax.annotate("Spermonde-archipel\n(museumexemplaren 1980–1986)",xy=(119.29,-5.08),xytext=(112.3,-3.2),fontsize=8.5,color=T2,arrowprops=dict(arrowstyle="-",color=T2,lw=0.8),zorder=6)
for name,x,y in [("Sulawesi",121.3,-2.0),("Borneo",113.5,0.5),("Java",109.5,-7.9),("Nieuw-Guinea",133.0,-3.6),("Banda-zee",126.4,-6.2)]:
    ax.text(x,y,name,fontsize=8.5,color=T2,style="italic",zorder=2,ha="center")
ax.set_xlim(*LON); ax.set_ylim(*LAT); ax.set_aspect("equal")
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(colors=T2,labelsize=7.5,length=0)
ax.set_xticks(range(105,136,5)); ax.set_yticks(range(-10,7,5))
ax.set_xticklabels([f"{x}°O" for x in range(105,136,5)]); ax.set_yticklabels([f"{abs(y)}°{'Z' if y<0 else ('N' if y>0 else '')}" for y in range(-10,7,5)])
ax.set_title("Ctenactis albitentaculata: gevonden in 1899 en nu",loc="left",fontsize=12.5,color=T1,pad=10,fontweight="bold")
leg=ax.legend(loc="lower left",fontsize=8,frameon=True,facecolor=SURF,edgecolor="#d6d4cd",labelcolor=T1,borderpad=0.7)
fig.text(0.01,0.01,"Bron: GBIF-records met coördinaten (taxonKey 2260588), opgehaald 31-10-2026; Siboga-exemplaar Naturalis ZMA.COEL.405. Kaartdata: Natural Earth.",fontsize=6.8,color=T2)
plt.tight_layout(rect=(0,0.03,1,1))
plt.savefig(sys.argv[3],facecolor=SURF)
print(len(obs),len(spc))
