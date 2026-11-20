"""Calcul de référence des indicateurs, indépendant de l'application.

Sert d'arbitre : chaque valeur affichée par l'application (avec ou sans
filtre) doit être identique à celle produite ici.

Usage :
    python3 scripts/reference.py docs/data [pays=FR] [annee=2016] [contrat=S]
"""
import json
import statistics
import sys


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    n, c, dic = d["n"], d["cols"], d["dicts"]
    rows = []
    for i in range(n):
        r = {k: c[k][i] for k in ("id", "year", "lots", "offers", "value", "poids", "cpv", "z")}
        for k in dic:
            code = c[k][i]
            r[k] = dic[k][code] if code >= 0 else None
        rows.append(r)
    return rows


def kpis(rows, pays=None, annee=None, contrat=None):
    f = [r for r in rows if (pays is None or r["pays"] == pays)
         and (contrat is None or r["contrat"] == contrat)]
    fa = [r for r in f if annee is None or r["year"] == annee]
    out = {"lignes": len(fa)}
    # KPI 1 et 2 : procédure ouverte, au moins une offre renseignée
    ope = [r for r in fa if r["proc"] == "OPE" and r["offers"] is not None and r["offers"] >= 1]
    num1 = sum(1 for r in ope if r["offers"] == 1)
    out["kpi1"] = (num1, len(ope), num1 / len(ope) if ope else None)
    out["kpi2_mediane_offres"] = (statistics.median([r["offers"] for r in ope]) if ope else None, len(ope))
    # KPI 3 : fenêtre 2016-2017 verrouillée (ignore le filtre année)
    w = [r for r in f if r["year"] in (2016, 2017)]
    ren = [r for r in w if r["pme"] is not None]
    num3 = sum(1 for r in ren if r["pme"] == "Y")
    out["kpi3"] = (num3, len(ren), num3 / len(ren) if ren else None)
    out["kpi3_taux_renseignement"] = (len(ren), len(w), len(ren) / len(w) if w else None)
    # KPI 5 : montant total pondéré, et médiane des montants (non pondérée)
    v = [r for r in fa if r["value"] is not None]
    out["kpi5_md_eur"] = (sum(r["value"] * r["poids"] for r in v) / 1e9, len(v))
    out["mediane_montant"] = (statistics.median([r["value"] for r in v]) if v else None, len(v))
    # KPI 5 (queue) : part du montant pondéré portée par le 1 % des plus gros montants
    vs = sorted(r["value"] for r in v)
    p99 = vs[int(0.99 * (len(vs) - 1))] if vs else None
    tot = sum(r["value"] * r["poids"] for r in v)
    top = sum(r["value"] * r["poids"] for r in v if r["value"] > p99)
    out["kpi5_part_top1pct"] = round(top / tot, 3) if tot else None
    # KPI 6 : part du montant pondéré portée par les attributions à z > 3
    zz = [r for r in fa if r["z"] is not None]
    z3 = [r for r in zz if r["z"] > 3]
    out["kpi6"] = (len(z3), len(zz), round(sum(r["value"] * r["poids"] for r in z3) / tot, 3) if tot else None)
    return out


def vue3(rows, seuil=0.40, cap=20, audit=500):
    """Contrôles de la vue 3 sans filtre : axe A (pays × secteur, procédure
    ouverte), axe B (pays, 2016-2017), axe C (liste d'audit des N plus forts z)."""
    from collections import defaultdict
    out = {}
    seg = defaultdict(lambda: [0, 0, 0.0])  # num, den, montant en jeu
    for r in rows:
        if r["proc"] != "OPE" or r["offers"] is None or r["offers"] < 1:
            continue
        s = seg[(r["pays"], (r["cpv"] or "??")[:2])]
        s[1] += 1
        if r["offers"] == 1:
            s[0] += 1
            s[2] += (r["value"] or 0) * r["poids"]
    total = sum(s[2] for s in seg.values())
    alert = sorted([(k, s) for k, s in seg.items() if s[1] >= 100 and s[0] / s[1] > seuil],
                   key=lambda t: -t[1][2])
    out["A_segments_alerte"] = len(alert)
    out["A_top3"] = [(k, s[0], s[1], round(s[0] / s[1], 3), round(s[2] / 1e9, 2)) for k, s in alert[:3]]
    covered = sum(s[2] for _, s in alert[:cap])
    out["A_couvert_Md"] = (round(covered / 1e9, 2), round(covered / sum(s[2] for _, s in alert), 3), round(covered / total, 3))
    b = defaultdict(lambda: [0, 0, 0])  # pme, renseignés, attributions
    for r in rows:
        if r["year"] in (2016, 2017):
            s = b[r["pays"]]
            s[2] += 1
            if r["pme"] is not None:
                s[1] += 1
                s[0] += r["pme"] == "Y"
    out["B_sous_40"] = sorted((k, s[0], s[1], round(s[0] / s[1], 3)) for k, s in b.items() if s[1] >= 100 and s[0] / s[1] < 0.40)
    sc = sorted((r for r in rows if r["z"] is not None), key=lambda r: -r["z"])
    lst = sc[:audit]
    w = lambda r: r["value"] * r["poids"]
    out["C_z_sup3"] = sum(1 for r in sc if r["z"] > 3)
    out["C_liste_couverture"] = round(sum(map(w, lst)) / sum(map(w, sc)), 4)
    uk = sum(1 for r in lst if r["pays"] == "UK")
    out["C_UK_liste"] = (uk, round(uk / audit, 3))
    return out


if __name__ == "__main__":
    base = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "vue3":
        for k, v in vue3(load(f"{base}/principal.json")).items():
            print(f"{k:22s} {v}")
        sys.exit()
    args = dict(a.split("=") for a in sys.argv[2:])
    if "annee" in args:
        args["annee"] = int(args["annee"])
    rows = load(f"{base}/principal.json")
    for k, v in kpis(rows, **args).items():
        print(f"{k:28s} {v}")
