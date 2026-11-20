# Fiche de paramétrage des mesures · application décisionnelle (séance 5)

**Observatoire européen des marchés publics** · Ingryd Lo Tierzo Silva et Sara Lhasseni · 20 novembre 2026
**URL publique** : https://amandacatarinoac-cmd.github.io/exobusinessintelligence/

## 1. Règles communes à toutes les mesures

| Règle | Application |
|---|---|
| Recalcul | Chaque indicateur est recalculé **à partir des lignes** à chaque changement de filtre (code : `docs/index.html`). Aucun agrégat figé, aucune moyenne de taux. Recalcul en moins de 60 ms sur 149 811 lignes. |
| Rapport d'agrégats | Numérateur et dénominateur sont comptés séparément ; le quotient est calculé à l'affichage ; les deux sont affichés à côté du taux. |
| Deux sources | Fichier principal (149 811 lignes) pour les vues 1 à 4 ; procédures rares (6 022 lignes) lues **à part**, procédure par procédure, en vue 4, sans aucun total. Les deux fichiers ne s'empilent jamais (erreur sanctionnée n° 11). |
| Dédoublonnage | Séance 2 : 334 doublons stricts retirés du principal (150 147 → 149 813) et 2 des rares (6 024 → 6 022), soit 336. Séance 5 : ID_AW 164662498 présent 3 fois, une seule ligne gardée (→ 149 811). |
| Valeurs sentinelles | NUMBER_OFFERS = 940 (281 lignes) et 999 (3 lignes) mis à vide : exclus des taux, des médianes et des effectifs d'offres. |
| Seuils d'effectif | 100 marchés pour les taux (KPI 1 à 3, segments des axes A et B) ; 100 marchés dans chaque groupe pour le KPI 4 ; 30 attributions pour les sommes et l'indice d'anomalie (KPI 5 et 6, segments de l'axe C) ; 30 attributions dans chaque groupe pour une strate de la vue 2. Sous le seuil : la valeur est remplacée par « effectif insuffisant » et **l'effectif reste affiché**. |
| Filtres de contexte | Pays, Année, Type de contrat, Secteur (division CPV). Ils s'appliquent à toutes les vues, sauf l'Année pour les KPI 3 et 4 et la relation R3 (fenêtre 2016-2017 verrouillée, signalée à l'écran). |

## 2. Les six indicateurs de la vue 1

| KPI | Formule implémentée | Numérateur | Dénominateur | Effectif affiché | Seuil | Sous le seuil | Valeur de contrôle (sans filtre) |
|---|---|---|---|---|---|---|---|
| **1** · Taux d'offre unique | num / dén | attributions en procédure ouverte avec exactement 1 offre | attributions en procédure ouverte avec au moins 1 offre renseignée | num / dén | dén ≥ 100 | « effectif insuffisant » + num / dén | **27,7 %** (32 573 / 117 468). Note S3 : 27,7 % (32 573 / 117 473) ; −5 au dénominateur : 3 lignes à 999 et 2 doublons de l'ID 164662498 |
| **2** · Médiane du nombre d'offres | médiane exacte sur les lignes (jamais une moyenne de médianes) | — | même population que le KPI 1 | N | N ≥ 100 | « effectif insuffisant » + N | **3 offres** (N = 117 468) ; note S3 : 3 |
| **3** · Part de PME | num / dén, fenêtre 2016-2017 | attributions 2016-2017 à une PME (B_CONTRACTOR_SME = Y) | attributions 2016-2017 avec la variable PME renseignée | num / dén + taux de renseignement (renseignés / attributions 2016-2017) | dén ≥ 100 | « effectif insuffisant » + num / dén | **53,7 %** (11 502 / 21 419), renseignement 53,7 % (21 419 / 39 881). Note S3 : 11 504 / 21 421 ; −2 : doublons de l'ID 164662498 |
| **4** · Écart ajusté du 6-10 lots | effet marginal moyen d'une régression logistique estimée **par pays** hors de l'outil (`scripts/prepare_data.py`, `docs/data/modeles.json`) | — | — | marchés à 6-10 lots et non allotis du pays | ≥ 100 dans **chaque** groupe | « non estimable » + effectifs ; avec un filtre contrat ou secteur : « non estimé pour ce sous-ensemble » | France **+8,8 pts [+1,1 ; +16,5]** (951 / 374) ; Allemagne −4,2 [−23,1 ; +14,8] ; Royaume-Uni −11,3 [−28,9 ; +6,3] ; effet moyen +3,2 [−1,7 ; +8,2]. Remplace le « gain simulé » +5,4 [+1,5 ; +9,2] de la S3 (rapport tous pays appliqué à la France) |
| **5** · Montant total pondéré | Σ (AWARD_VALUE_EURO × POIDS) | — | — | N attributions + médiane non pondérée par attribution | N ≥ 30 | « effectif insuffisant » + N | **3 213,3 Md€** (N = 149 811) ; note S3 : 3 213 Md€. Médiane : **45 780 €** (note : 45 781 €, écart dû aux 2 doublons retirés). Part portée par le 1 % des plus gros montants : 69,4 % |
| **6** · Part du montant des attributions atypiques | Σ montant pondéré des lignes à z > 3 / Σ montant pondéré | montant pondéré des attributions à z > 3 | montant pondéré du périmètre | nombre d'attributions à z > 3 / attributions scorées | N ≥ 30 | « effectif insuffisant » + N | **28,8 %** (566 / 149 811 attributions). Ancien indice S4 (strate CPV × contrat) : 489 attributions, 36,4 % |

**Prix à payer du KPI 4 (R2)**, affiché sur la carte : offre unique des 6-10 lots / offre unique des non allotis, procédure ouverte, filtres appliqués ; seuil 100 dans chaque groupe. Sans filtre : 30,6 % (3 242 / 10 612) contre 20,2 % (7 771 / 38 504), soit +10,4 points.

## 3. Les deux mesures préparées hors de l'outil

| Mesure | Modèle | Population | Ce qui se recalcule à l'écran | Ce qui est figé |
|---|---|---|---|---|
| **Indice d'anomalie z** (KPI 6, axe C, vue 4) | Régression linéaire du log10 du montant sur secteur × contrat, pays, année, classe de lots (inconnu, non alloti, 1, 2-5, 6-10, 11+), procédure ; z robuste = (résidu − médiane) / (1,4826 × écart absolu médian) | 149 811 attributions ; R² = 0,39 | Toutes les sommes, parts, listes et compositions construites à partir du z de chaque ligne | Le z de chaque ligne et le montant attendu (une colonne par ligne) |
| **Écart ajusté du 6-10 lots** (KPI 4) | Régression logistique PME ~ 6-10 lots + log10 du montant + contrat + année, estimée pour chaque pays ; effet marginal moyen et IC 95 % (méthode delta) ; effet moyen avec effet pays | 2016-2017, PME renseignée, 6-10 lots contre non allotis : 2 488 et 1 221 marchés | Le choix du pays affiché | L'estimation (affichée seulement là où elle existe, jamais sous un filtre contrat ou secteur) |

## 4. Mesures de la vue 3 (segmentation)

| Axe | Mesure | Formule | Seuil | Contrôle (sans filtre) |
|---|---|---|---|---|
| A | Montant en jeu d'un segment | Σ montant × POIDS des attributions à offre unique du segment (procédure ouverte, ou procédures avec mise en concurrence si le croisement inclut la procédure ; NOC et AWP signalées et hors classement) | 100 marchés | Pologne × 33 : 17,47 Md€, 48,5 % (12 917 / 26 643) |
| A | Segments en alerte, dossiers retenus | taux > seuil choisi (30, 40, 50 %) ; les N premiers par montant en jeu (N de 1 à 60) | 100 marchés | 21 segments à 40 % (41 à 30 %, 7 à 50 %) ; N = 20 → 36,09 Md€, 99,9 % du montant en jeu des segments en alerte, 21,4 % de la dépense à offre unique |
| A | Liste de surveillance | sous le seuil d'alerte et médiane des offres ≤ 2 | 100 marchés | 26 segments (47 à médiane ≤ 2 = 21 en alerte + 26) |
| B | Part de PME, taux de renseignement, part non allotie | PME / renseignés ; renseignés / attributions ; non allotis / lots connus (2016-2017) | 100 renseignés | Espagne 31,2 % (197 / 631), Italie 31,7 % (148 / 467), Autriche 31,7 % (52 / 164), Norvège 29,0 % (40 / 138) |
| B | Enjeu | Σ montant × POIDS des non allotis 2016-2017 | — | 14,73 Md€ pour les 4 pays en revue |
| C | Liste d'audit | les N attributions au z le plus élevé (N = 100, 500, 1 000 ou 5 % du périmètre) | — | N = 500 : 27,6 % du montant pondéré |
| C | Composition par pays | part de la liste ; part des attributions ; part du montant ; part du montant sans le dernier centile | — | Royaume-Uni : 16,6 % (83 / 500), 3,5 %, 42,3 %, 11,0 % |
| C | Segments atypiques | Σ montant pondéré des lignes à z > 3 du segment | 30 attributions | Royaume-Uni × 79 : 119,67 Md€ (22 / 473) |

## 5. Mesures de la vue 2 (analyse)

| Mesure | Formule | Seuil |
|---|---|---|
| Taux par groupe | résultat = 1 / effectif du groupe, affiché pour les deux groupes | — |
| Rapport de cotes et IC 95 % | (a × d) / (b × c), IC de Woolf ; correction de 0,5 si une case est vide | strate : ≥ 30 dans chaque groupe (règle S3) |
| Écart en points | p1 − p0, IC de Wald | — |
| Ajustement sur le confondant | Mantel-Haenszel sur toutes les strates, IC de Robins-Breslow-Greenland | — |
| R4 (montant) | d de Cohen sur log10 du montant (écart-type commun) ; rapport des médianes ; ajustement : moyenne des d des strates pondérée par l'inverse de la variance | strate : ≥ 30 dans chaque groupe |

Contrôles contre la note S3 : R1 0,62 [0,57 ; 0,66], ajusté sur le pays 0,60 ; R2 1,46 [1,40 ; 1,53], +7,3 points ; R3 1,30 [1,13 ; 1,49], ajusté sur la valeur 1,15 [0,99 ; 1,33]. R4 : d = 0,43 (note : 0,43) ; strate fournitures 0,30 (note : 0,35), écart de méthode consigné (registre E20).

## 6. Contrôles filtrés : écran contre calcul manuel

Le calcul manuel est fait **directement sur le fichier Excel FINAL** (pandas), indépendamment du code de l'application.

| Sélection | KPI 1 | KPI 2 | KPI 3 | KPI 5 | Médiane des montants | Écran = calcul ? |
|---|---|---|---|---|---|---|
| France × 2016 | 12,3 % (317 / 2 587) | 4 | 45,3 % (2 740 / 6 045) | 44,9 Md€ (3 229) | 88 135 € | ✅ |
| Royaume-Uni | 9,1 % (254 / 2 795) | 5 | 53,1 % (641 / 1 208) | 1 357,7 Md€ (5 266) | 393 223 € | ✅ (via `reference.py`) |
| Pologne × 2015 × fournitures | 46,9 % (1 983 / 4 224) | 2 | 54,1 % (1 979 / 3 657) | 5,4 Md€ (4 421) | 6 410 € | ✅ |
| Malte × 2016 × travaux | effectif insuffisant (0 / 4) | effectif insuffisant | effectif insuffisant (3 / 3) | effectif insuffisant (4) | — | ✅ comportement sous le seuil |

Pour la Pologne et le Royaume-Uni, le KPI 3 ignore le filtre Année (fenêtre 2016-2017) ; le calcul manuel applique la même règle.
