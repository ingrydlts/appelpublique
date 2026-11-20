"""Préparation des données de l'application (séance 5).

Lit les deux fichiers FINAL de la séance 3 et écrit deux fichiers JSON
séparés pour l'application. Les deux sources ne sont JAMAIS empilées
(erreur sanctionnée n° 11 du cours).

Usage :
    python3 scripts/prepare_data.py <principal.xlsx> <rares.xlsx> <dossier_sortie>

Règles appliquées en plus du nettoyage de la séance 3 (déjà dans les FINAL) :
  R-S5-1  ID_AW 164662498 présent 3 fois (seul le poids du prix diffère :
          60, 50, 40). Grain = une attribution : on garde la première ligne.
  R-S5-2  NUMBER_OFFERS = 999 (3 lignes, BG 2014, même acheteur, 45 lots) :
          traité comme la sentinelle 940, mis à vide et signalé.
Chaque règle est consignée dans le registre des écarts.
"""
import json
import sys

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

ID_TRIPLE = 164662498
SENTINELLE_999 = 999


def encode_cat(series):
    """Encodage par dictionnaire : renvoie (modalités, codes ; -1 = vide)."""
    s = series.astype("string")
    cats = sorted(s.dropna().unique().tolist())
    idx = {c: i for i, c in enumerate(cats)}
    codes = [idx[v] if v is not pd.NA and v in idx else -1 for v in s.tolist()]
    return cats, codes


def num(series, nd=None):
    out = []
    for v in series.tolist():
        if pd.isna(v):
            out.append(None)
        elif nd is None:
            out.append(int(v))
        else:
            out.append(round(float(v), nd))
    return out


def lots_class(x):
    if pd.isna(x):
        return "inconnu"
    x = int(x)
    if x == 0:
        return "non alloti"
    if x == 1:
        return "1"
    if x <= 5:
        return "2-5"
    if x <= 10:
        return "6-10"
    return "11+"


def robust_z(r):
    med = np.median(r)
    mad = np.median(np.abs(r - med)) * 1.4826
    return (r - med) / mad


def anomaly(p):
    """KPI 6 · indice d'anomalie (retour du rendu 4, priorité 2).

    Résidu de la régression du log10 du montant sur ce que le marché
    annonce : secteur (division CPV) × type de contrat, pays, année,
    classe de lots, procédure. z robuste = (résidu − médiane) / (1,4826 × MAD).
    L'ancienne version (S4) n'utilisait que la strate CPV × contrat ;
    elle est recalculée ici pour chiffrer l'écart dans le registre.
    """
    d = pd.DataFrame({
        "lv": p["AWARD_VALUE_LOG10"],
        "cpvdiv": p["CPV"].astype("string").str[3:5].fillna("NA"),
        "contrat": p["TYPE_OF_CONTRACT"].astype("string").fillna("NA"),
        "pays": p["ISO_COUNTRY_CODE"].astype("string").fillna("NA"),
        "year": p["YEAR"].astype(str),
        "lots": p["LOTS_NUMBER"].map(lots_class),
        "proc": p["TOP_TYPE"].astype("string").fillna("NA"),
    })
    ok = d["lv"].notna()
    fit = smf.ols("lv ~ C(cpvdiv):C(contrat) + C(pays) + C(year) + C(lots) + C(proc)",
                  data=d[ok].astype({c: str for c in d.columns if c != "lv"})).fit()
    z = pd.Series(np.nan, index=p.index)
    z[ok] = robust_z(fit.resid.to_numpy())
    pred = pd.Series(np.nan, index=p.index)
    pred[ok] = np.power(10.0, fit.fittedvalues.to_numpy())  # montant attendu au regard des caractéristiques
    z = z.round(2)  # précision publiée : les comptes du journal utilisent la même valeur que l'application
    # Ancienne strate S4 (CPV × contrat), pour comparaison seulement.
    strat = d[ok].groupby(["cpvdiv", "contrat"])["lv"]
    z_old = (d.loc[ok, "lv"] - strat.transform("mean")) / strat.transform("std")
    w = (p["AWARD_VALUE_EURO"] * p["POIDS"])[ok]
    comp = {
        "modele_r2": round(fit.rsquared, 3), "n_modele": int(fit.nobs),
        "z_sup3_nouveau": int((z[ok] > 3).sum()),
        "part_montant_z_sup3_nouveau": round(float(w[z[ok] > 3].sum() / w.sum()), 3),
        "z_sup3_ancien_cpv_contrat": int((z_old > 3).sum()),
        "part_montant_z_sup3_ancien": round(float(w[z_old > 3].sum() / w.sum()), 3),
    }
    return z, pred, comp


def kpi4(p, seuil=100):
    """KPI 4 · écart ajusté du 6-10 lots sur la part de PME (ex « gain simulé »).

    Retour du rendu 4, priorité 1 : estimé PAR PAYS, avec son intervalle,
    publié seulement là où il est estimable (au moins `seuil` marchés dans
    chaque groupe). Population : 2016-2017, PME renseignée, 6-10 lots
    contre non allotis. Modèle logistique PME ~ 6-10 lots + log10(montant)
    + contrat + année. Écart ajusté = effet marginal moyen du passage à
    6-10 lots, en points de part de PME (IC 95 %, méthode delta).
    Lecture : association ajustée, hétérogène ; pas un effet causal.
    """
    w = pd.DataFrame({
        "y": p["B_CONTRACTOR_SME"].eq("Y").astype(int), "pme": p["B_CONTRACTOR_SME"],
        "lots": p["LOTS_NUMBER"], "lv": p["AWARD_VALUE_LOG10"], "year": p["YEAR"].astype(str),
        "contrat": p["TYPE_OF_CONTRACT"].astype(str), "pays": p["ISO_COUNTRY_CODE"].astype(str),
    })
    w = w[p["YEAR"].isin([2016, 2017]) & w["pme"].notna() & w["lots"].notna() & w["lv"].notna()]
    w = w[w["lots"].eq(0) | w["lots"].between(6, 10)].copy()
    w["g"] = (w["lots"] > 0).astype(int)

    def fit(df, formula):
        m = smf.logit(formula, data=df).fit(disp=0)
        me = m.get_margeff(at="overall", dummy=True).summary_frame().loc["g"]
        ci = m.conf_int().loc["g"]
        return {
            "or": round(float(np.exp(m.params["g"])), 2),
            "or_lo": round(float(np.exp(ci[0])), 2), "or_hi": round(float(np.exp(ci[1])), 2),
            "ecart_pts": round(float(me["dy/dx"]) * 100, 1),
            "ecart_lo": round(float(me["Conf. Int. Low"]) * 100, 1),
            "ecart_hi": round(float(me["Cont. Int. Hi."]) * 100, 1),
        }

    out = {"seuil_par_groupe": seuil, "pays": {}}
    for pays, df in w.groupby("pays"):
        n1, n0 = int(df["g"].sum()), int((df["g"] == 0).sum())
        e = {"n_6_10": n1, "n_non_alloti": n0,
             "pme_6_10": int(df.loc[df["g"] == 1, "y"].sum()), "pme_non_alloti": int(df.loc[df["g"] == 0, "y"].sum())}
        if n1 >= seuil and n0 >= seuil:
            e.update(fit(df, "y ~ g + lv + C(contrat) + C(year)"))
        out["pays"][pays] = e
    tot = {"n_6_10": int(w["g"].sum()), "n_non_alloti": int((w["g"] == 0).sum()),
           "pme_6_10": int(w.loc[w["g"] == 1, "y"].sum()), "pme_non_alloti": int(w.loc[w["g"] == 0, "y"].sum())}
    tot.update(fit(w, "y ~ g + lv + C(contrat) + C(year) + C(pays)"))
    out["ensemble_effet_moyen"] = tot
    return out


def build(df, cats_cols, journal):
    cols, dicts = {}, {}
    cols["id"] = num(df["ID_AW"])
    cols["year"] = num(df["YEAR"])
    cols["lots"] = num(df["LOTS_NUMBER"])
    cols["offers"] = num(df["NUMBER_OFFERS"])
    cols["awards"] = num(df["NUMBER_AWARDS"])
    cols["value"] = num(df["AWARD_VALUE_EURO"], 2)
    cols["poids"] = num(df["POIDS"], 2)
    cols["cpv"] = [None if pd.isna(c) else str(c).replace("CPV", "") for c in df["CPV"].tolist()]
    if "Z" in df.columns:
        cols["z"] = num(df["Z"], 2)
        cols["pred"] = num(df["PRED"].round(0))
    for key, col in cats_cols.items():
        dicts[key], cols[key] = encode_cat(df[col])
    return {"n": len(df), "dicts": dicts, "cols": cols, "journal": journal}


def main(p_path, r_path, out_dir):
    cats = {
        "pays": "ISO_COUNTRY_CODE", "contrat": "TYPE_OF_CONTRACT", "proc": "TOP_TYPE",
        "pme": "B_CONTRACTOR_SME", "enchere": "B_ELECTRONIC_AUCTION", "crit": "CRIT_CODE",
        "acheteur": "CAE_TYPE",
    }

    p = pd.read_excel(p_path, sheet_name=0)
    n_final = len(p)
    dup_mask = p["ID_AW"].eq(ID_TRIPLE) & p.duplicated("ID_AW", keep="first")
    n_dup = int(dup_mask.sum())
    p = p[~dup_mask].copy()
    m999 = p["NUMBER_OFFERS"].eq(SENTINELLE_999)
    n999 = int(m999.sum())
    p.loc[m999, "NUMBER_OFFERS"] = pd.NA
    journal_p = {
        "lignes_brutes": 150147, "doublons_stricts_s3": 334, "lignes_final": n_final,
        "id_triple_retire": n_dup, "sentinelle_999_mise_a_vide": n999,
        "sentinelle_940_deja_isolee": int(p["NUMBER_OFFERS_SENTINELLE"].sum()),
        "lignes_application": len(p),
    }
    z, pred, comp = anomaly(p)
    p["Z"] = z
    p["PRED"] = pred
    journal_p["indice_anomalie"] = comp
    k4 = kpi4(p)
    with open(f"{out_dir}/modeles.json", "w", encoding="utf-8") as fh:
        json.dump({"kpi4": k4}, fh, ensure_ascii=False, separators=(",", ":"))
    print("kpi4", {k: v for k, v in k4["pays"].items() if "or" in v}, k4["ensemble_effet_moyen"])
    r = pd.read_excel(r_path, sheet_name=0)
    journal_r = {"lignes_brutes": 6024, "doublons_stricts_s3": 2, "lignes_final": len(r),
                 "lignes_application": len(r)}

    for name, df, jr in (("principal", p, journal_p), ("rares", r, journal_r)):
        data = build(df, cats, jr)
        with open(f"{out_dir}/{name}.json", "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        print(name, jr)


if __name__ == "__main__":
    main(*sys.argv[1:4])
