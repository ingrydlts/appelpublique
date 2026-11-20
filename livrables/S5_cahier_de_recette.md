# Cahier de recette · application décisionnelle (séance 5)

**Observatoire européen des marchés publics** · Ingryd Lo Tierzo Silva et Sara Lhasseni · 20 novembre 2026
**URL publique testée** : https://amandacatarinoac-cmd.github.io/exobusinessintelligence/ (sans authentification)

## Méthode

1. **Exécution de chaque story sur l'application en ligne**, dans un navigateur vierge (sans cookies ni session, équivalent d'une navigation privée). On suit le chemin prévu, on compte les clics, on relève la réponse affichée et on la compare au calcul de référence (`scripts/reference.py`).
2. **Chronométrage par une personne** : colonne « Temps » à remplir en jouant chaque story une fois avec un chronomètre. **La story du décideur politique échoue au-delà de deux minutes.**
3. **Diagnostic de chaque échec** : filtre manquant, mesure mal codée ou story mal écrite (consigne S5), puis correction apportée et nouvel essai.
4. **Test par une autre équipe** sur une question qu'elle formule elle-même (section 4).

## 1. Stories réécrites après le retour sur le rendu 4

| N° | Version S4 | Version recettée | Pourquoi |
|---|---|---|---|
| 1 | … classer les segments pays × secteur **par taux d'offre unique** … | En tant que responsable de la surveillance, je veux classer les segments pays × secteur en procédure ouverte **par montant en jeu** (dépense à offre unique), avec leur taux, leur effectif et ma **capacité d'instruction N**, afin de retenir les dossiers à instruire en 2018. | Contredisait la vue 3, qui trie par valeur en jeu |
| 7 | … vérifier d'abord la queue de distribution avant d'orienter l'audit | En tant que responsable de la surveillance, je veux savoir si la part d'un pays dans le montant pondéré **résiste au retrait du dernier centile**, afin de décider si l'audit vise ce pays ou seulement les quelques marchés qui portent sa part. | C'était un contrôle de qualité, pas une décision. Couverte dans la recette par la story 12 |
| 10 | … voir les six indicateurs … **puis descendre vers un cas** … | En tant que décideur politique, je veux lire **sur la seule vue 1, sans manipulation**, les six indicateurs avec leurs effectifs et leurs alertes, afin de choisir l'axe à porter à l'arbitrage. | Le décideur ne passe pas plus de deux minutes dans l'outil |
| 12 | **Décideur politique** … voir que le Royaume-Uni pèse 42 % … filtre pays | En tant qu'**analyste** de l'Observatoire, je veux comparer pour chaque pays sa part de la liste d'audit, sa part des attributions et sa part du montant **avec et sans le dernier centile**, afin de décider si la liste d'audit doit être répartie par quota de pays. | Pondérer l'audit par pays est une décision d'analyste ; le chiffre de 42 % dépend de la queue |

Les stories 5 et 8 sont reformulées à la marge : « gain attendu » devient « écart ajusté » (KPI 4 renommé), et la story 8 vise **une seule liste d'audit** de N attributions au lieu de mélanger les 489 marchés à z > 3 et l'audit de 5 %.

## 2. Synthèse de la recette

Profils : **RS** responsable de la surveillance, **AN** analyste de l'Observatoire, **DP** décideur politique.

| N° | Profil | Axe | Vues | Clics | Résultat | Temps | Cause de l'échec | Correction |
|---|---|---|---|---|---|---|---|---|
| 1 | RS | A | 3 | 1 | ✅ Réussite | ___ | — | — |
| 2 | RS | A | 3 | 2 | ⚠️ Échec au premier essai, ✅ après correction | ___ | **Filtre manquant** : le tableau s'arrêtait aux 40 premiers segments, 19 des 26 segments en surveillance étaient visibles | Filtre « Afficher » par statut ajouté ; les 26 segments s'affichent |
| 3 | AN | A | 2 | 1 | ✅ Réussite | ___ | — | — |
| 4 | RS | B | 1 → 3 | 1 | ✅ Réussite | ___ | — | — |
| 5 | DP | B | 1 | 0 | ⚠️ Échec au premier essai, ✅ après correction | ___ (< 2 min exigé) | **Mesure absente de la vue** : le coût en offre unique (R2) n'était qu'en vue 2 ; le décideur aurait dû naviguer | « Prix à payer (R2) » recalculé et affiché sur la carte du KPI 4 |
| 8 | RS | C | 3 → 4 | 3 | ✅ Réussite | ___ | — | — |
| 10 | DP | A, B, C | 1 | 0 | ✅ Réussite | ___ (< 2 min exigé) | Échouait en S4 (story mal écrite : le décideur descendait jusqu'à un cas) | Story réécrite : lecture seule de la vue 1 |
| 12 | AN | C | 3 | 2 | ✅ Réussite | ___ | Échouait en S4 (story mal écrite : décideur, 42 % non testé) | Story réécrite ; test du dernier centile intégré à la vue 3 |

**Bilan** : 8 stories sur 8 exécutables après correction ; 2 échecs diagnostiqués et corrigés pendant la recette (un filtre manquant, une mesure absente de la vue du décideur) ; 2 échecs de conception de la S4 corrigés par réécriture. Le temps reste à chronométrer.

## 3. Détail par story

### Story 1 · Retenir les dossiers à instruire en 2018 (axe A)
- **Chemin** : onglet 3 · Segmentation → axe A (par défaut), seuil 40 %, capacité N = 20.
- **Résultat obtenu** : 21 segments en alerte (> 40 %, au moins 100 marchés) ; 20 dossiers retenus couvrant **36,09 Md€** de montant en jeu, soit 99,9 % des segments en alerte et 21,4 % de toute la dépense à offre unique (168,29 Md€). En tête : Pologne × 33 (matériel médical), 48,5 % (12 917 / 26 643), 17,47 Md€ en jeu ; puis Pologne × 77 (61,4 %, 3,01 Md€).
- **Contrôle** : identique à `reference.py vue3` (21 segments, 36,09 Md€).
- **Avec le filtre Année = 2017** (années récentes) : 5 segments en alerte, 3,47 Md€ couverts. Le filtre répond bien à la story.
- **Décision** : instruire les 20 segments dans l'ordre du montant en jeu, pas du taux (Roumanie × 85, à 71,5 % sur 179 marchés, ne passe pas devant Pologne × 33).

### Story 2 · Liste de surveillance (axe A)
- **Chemin** : vue 3 → axe A → Afficher : Surveillance.
- **Premier essai** : l'indicateur annonçait 26 segments, mais seuls 19 étaient visibles dans le tableau limité à 40 lignes. **Échec, filtre manquant.**
- **Après correction** : 26 segments affichés, triés par montant en jeu ; en tête Pologne × 90 (32,1 %, médiane 2, 4,78 Md€).
- **Cohérence avec la note S3** : 47 segments ont une médiane ≤ 2 = 21 en alerte (instruits) + 26 sous le seuil (surveillés).
- **Décision** : inscrire les 26 segments en liste de surveillance.

### Story 3 · Où l'action « enchère » a-t-elle un fondement ? (axe A)
- **Chemin** : onglet 2 · Analyse → R1 (par défaut), stratification par pays (par défaut), périmètre procédure ouverte.
- **Résultat obtenu** : brut 20,7 % (971 / 4 690) avec enchère contre 29,1 % (29 546 / 101 649) sans, rapport de cotes 0,64 [0,59 ; 0,68] ; ajusté sur le pays 0,66 [0,61 ; 0,72]. Par pays : Pologne 0,40 [0,34 ; 0,45], Tchéquie 0,12 [0,06 ; 0,27], Hongrie 0,16 [0,07 ; 0,35] : association établie ; Roumanie 0,91 [0,80 ; 1,03] : non établie en procédure ouverte ; France 1,37 [0,84 ; 2,22] : non établie ; Italie 1,95 [1,26 ; 3,01] : **sens inverse**. L'écran signale une association hétérogène.
- **Décision** : promouvoir l'enchère en Pologne, Tchéquie et Hongrie ; ne pas l'imposer en France ni en Italie. **Écart avec la S3** : la Roumanie n'est établie qu'en incluant toutes les procédures (bouton « Toutes procédures »), pas en procédure ouverte.

### Story 4 · Revue d'allotissement (axe B)
- **Chemin** : vue 1 → KPI 3 « Où agir ? pays sous 40 % » → vue 3, axe B.
- **Résultat obtenu** : 4 pays sous 40 % de PME avec au moins 100 renseignés : Espagne 31,2 % (197 / 631), Italie 31,7 % (148 / 467), Autriche 31,7 % (52 / 164), Norvège 29,0 % (40 / 138), identiques à la note S3. Taux de renseignement : 32 %, 32 %, **72 %**, 44 %. Enjeu non alloti de ces quatre pays : 14,73 Md€.
- **Décision** : ouvrir la revue d'allotissement d'abord en Autriche, seul pays renseigné à plus de 50 % ; pour l'Espagne, l'Italie et la Norvège, faire vérifier le renseignement de la variable PME avant toute revue.

### Story 5 · Lancer ou non le 6-10 lots (axe B, décideur)
- **Chemin** : vue 1, carte 4, lecture seule. **0 clic.**
- **Premier essai** : l'écart ajusté était lisible, mais son coût en offre unique ne figurait qu'en vue 2. **Échec, mesure absente de la vue du décideur.**
- **Après correction** : « Écart ajusté du 6-10 lots : France **+8,8 points [+1,1 ; +16,5]** » (951 marchés à 6-10 lots, 374 non allotis), seul pays où l'association est établie ; Allemagne et Royaume-Uni non établis ; effet moyen tous pays +3,2 [−1,7 ; +8,2], non établi. Prix à payer (R2, procédure ouverte) : +10,4 points d'offre unique tous pays ; en filtrant sur la France, +3,5 points (415 / 2 767 contre 529 / 4 615).
- **Décision** : pas de généralisation ; au mieux un pilote encadré en France, avec condition d'arrêt. **Point d'attention** : la condition d'invalidation de la S3 (« moins de +1,5 point de PME ») tombe dans l'intervalle français.

### Story 8 · Constituer la liste d'audit (axe C)
- **Chemin** : vue 3 → axe C (N = 500 par défaut) → « Voir toute la liste d'audit » → vue 4, triée par indice d'anomalie ; filtre Type de contrat pour la lire par contrat.
- **Résultat obtenu** : 500 attributions, **27,6 %** du montant pondéré (885,33 Md€ / 3 213,31 Md€), toutes à z > 3. En tête : ID_AW 115005289 (Pologne, 2012), 354,7 M€ pour 4 126 € attendus. Avec Contrat = Travaux : 34 attributions.
- **Décision** : ouvrir la fiche de chaque attribution, écarter les gros lots légitimes et les erreurs de saisie, garder le reste pour l'audit.

### Story 10 · Choisir l'axe à porter à l'arbitrage (décideur)
- **Chemin** : vue 1, lecture seule. **0 clic.**
- **Résultat obtenu** : KPI 1 27,7 % (sous 40 %) ; KPI 2 3 offres ; KPI 3 53,7 % (au-dessus de 40 %) ; KPI 4 France +8,8 points [+1,1 ; +16,5] ; KPI 5 3 213,3 Md€, **dont 69 % portés par 1 % des montants (alerte)** ; KPI 6 28,8 % du montant porté par les attributions atypiques. Chaque carte montre son effectif sans clic.
- **Décision** : l'alerte porte sur l'axe C (budget). C'est lui que le décideur porte à l'arbitrage, la concentration du montant appelant d'abord un audit ciblé.

### Story 12 · Faut-il répartir l'audit par pays ? (axe C, analyste)
- **Chemin** : vue 3 → axe C → tableau « Liste d'audit : qui y pèse ? ».
- **Résultat obtenu** : Royaume-Uni 16,6 % de la liste (83 / 500) pour 3,5 % des attributions ; il pèse 42,3 % du montant pondéré, mais **11,0 % sans le dernier centile**. Lettonie 18,2 % de la liste (91 / 500) pour 2,6 % des attributions. Pologne 15,2 % de la liste pour 30,4 % des attributions.
- **Décision** : pas de quota par pays fondé sur le montant, car le poids du Royaume-Uni tient à quelques très gros marchés. Examiner en priorité la surreprésentation de la Lettonie (fiches en vue 4) avant de trancher.

## 4. Test par une autre équipe

À remplir pendant la séance 6 (21 novembre), ou avant si un membre d'une autre équipe est disponible.

| Testeur (équipe) | Question formulée par le testeur | Chemin suivi | Réponse obtenue | Temps | Réussite ? | Si échec : filtre manquant, mesure mal codée ou story absente ? |
|---|---|---|---|---|---|---|
| | | | | | | |

**Pré-test interne** (question non prévue, choisie hors des stories) : « Quelle part des marchés de travaux en Roumanie en 2015 a reçu une seule offre ? » En 3 clics (Pays, Année, Contrat), la vue 1 répond **« effectif insuffisant »** avec l'effectif affiché (1 / 16 marchés). Le croisement passe sous le seuil de 100 et l'application le dit au lieu de publier un taux fragile.

## 5. Ce que la recette a changé dans l'application

- Ajout d'un filtre de statut dans la vue 3, axe A (story 2).
- Ajout du prix à payer (R2) sur la carte du KPI 4 en vue 1 (story 5).
- Stories 1, 7, 10 et 12 réécrites (section 1).
