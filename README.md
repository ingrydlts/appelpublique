# EXOAPPELPUBLIQUE · Observatoire européen des marchés publics

Projet fil rouge du cours **BI, Dashboards & Data Storytelling** (Master 2, Programme Grande École, Paris School of Business). Enseignant : Olivier Mamavi, professeur associé. Auteures : Ingryd Lo Tierzo Silva et Sara Lhasseni.

Ce dépôt documente les décisions clés du projet, les consignes, l'historique des rendus et le plan de travail en cours. Il ne contient ni les données brutes ni les enregistrements de cours.

**Application en ligne (sans authentification) : https://amandacatarinoac-cmd.github.io/exobusinessintelligence/**

**Rendu du 20 novembre 2026 (séance 5)** : application complète en quatre vues, cahier de recette, registre des écarts, fiche de paramétrage des mesures et journal de bord (dossier `livrables/`). Reste à faire par l'équipe : chronométrer les stories, faire tester l'application par une autre équipe, ouvrir l'URL depuis un autre poste en navigation privée. Revue croisée le 21 novembre (séance 6). Voir la section 5.

## 1. Le projet en bref

| Élément | Contenu |
| --- | --- |
| Rôle | Consultante data pour la Commission européenne |
| Client | L'Observatoire des marchés publics, qui vérifie que les achats publics fonctionnent bien dans toute l'Europe |
| Données | Deux fichiers disjoints : un échantillon principal (150 147 lignes brutes) et les procédures rares (6 024 lignes brutes), 22 colonnes, 2009-2017, 33 pays. Une ligne est une **attribution**, pas un marché (identifiant ID_AW). Après dédoublonnage de 336 lignes : 155 835 lignes au total. Les deux fichiers ne s'empilent jamais |
| Livrable final | Une application web interactive, ouverte par une URL publique sans authentification, en quatre vues : globale, analyse, segmentation, exploration |
| Mission | Préparer l'exercice de surveillance 2018 : non pas décrire le marché, mais décider où agir |

Trois questions, chacune avec une variable imposée à expliquer. La séance 5 reformule les décisions à outiller.

| Axe | Question | Variable cible | Décision à outiller (séance 5) |
| --- | --- | --- | --- |
| A · Concurrence | Où y a-t-il trop peu d'entreprises qui répondent ? | NUMBER_OFFERS | Sur quels segments déclencher une revue pour maximiser la dépense replacée en concurrence effective, avec la capacité d'instruction ? |
| B · PME | Comment aider les petites entreprises à gagner ? | B_CONTRACTOR_SME | Quel dispositif d'allotissement recommander, sur quel périmètre, avec quel gain attendu et quel effet indésirable ? |
| C · Budget | Où l'argent public est-il dépensé de façon anormale ? | AWARD_VALUE_EURO | Où concentrer l'audit, sur quels segments aux montants anormaux au regard de leurs caractéristiques ? |

Idée centrale du cours : la BI sert à aider à décider. Un tableau de bord est une hypothèse causale rendue visible et vérifiable, pas une pile de graphiques. Règle qui commande tout : **un indicateur se recalcule à chaque filtre, il ne se moyenne jamais.**

## 2. Calendrier et historique des rendus

| Date | Séance ou rendu | Contenu | Statut |
| --- | --- | --- | --- |
| Avant le 26 sept. | S1 · Onboarding | Rôles et journal de bord, trois axes reformulés en problèmes décisionnels sous contrainte, confrontation des indicateurs officiels de la Commission (soumissionnaire unique, part des PME), URL publique vide. Power BI exclu sans validation écrite | Rendu |
| 26 sept. 2026 | S2 · Description et analyse des données | Note d'audit de 3 pages : grain, six anomalies chiffrées, périmètre d'exploitabilité, choix statistiques, journal des transformations. Dictionnaire des distributions | Rendue, corrigée sur quatre points dans la note de la S3 |
| 3 oct. 2026 | S3 · Hypothèses | Hypothèses H1 à H6 écrites avant tout test ; bases nettoyées (fichiers FINAL) | Déposées |
| 5 et 13 oct. | S3 · Étapes 1 à 4 | Base consolidée, variables, hypothèses, relations explorées et contrôlées ; version harmonisée du 13 octobre ; carte causale | Rendues |
| 13 oct. 2026 | S3 · Étape 5 | Note de tests et de conception : six fiches KPI, carte causale à quatre niveaux, recommandation du 6-10 lots | Rendue |
| 17 oct. 2026 | S4 · Architecture décisionnelle | Présentation de la note par Ingryd et Sara, puis travail d'architecture : modèle de données, quatre vues maquettées, huit user stories | Faite |
| Novembre 2026 | Rendu 4 | `livrables/S4_BI_Livrable_Observatoire_marches_publics.docx` : note de modélisation, maquettes annotées, user stories, annexe sur le choix des six KPI | Rendu, évalué, voir section 3 |
| 14 nov. 2026 | S5 · Construction de l'application | Couche de mesures, vues globale et segmentation. Livrable de fin de séance : URL publique et fiche de paramétrage des mesures | URL et fiche livrées le 19-20 nov. avec l'application |
| 19 nov. 2026 | Prototype HTML | Fichier « Observatoire européen des marchés publics · Tableau de bord.html » (vues 1 à 4) | Diagnostiqué : seules les procédures rares étaient recalculées, tout le fichier principal était écrit en dur. Conservé comme maquette, remplacé par `docs/index.html` |
| **20 nov. 2026** | **S5 · Échéance** | Application complète, cahier de recette, registre des écarts, journal de bord | **Livré** (chronométrage et test par une autre équipe à compléter) |
| 21 nov. 2026 | S6 · Revue croisée | Une autre équipe teste l'application sur une question qu'elle formule ; la séance audite ce qui est livré le 20 | À préparer |
| Plus tard | S7 et S8 | Recommandations, puis jury (soutenance) | |

## 3. Retour reçu sur le rendu de la séance 4

Le retour reconnaît que toutes les exigences de la séance 4 sont traitées et que les chiffres principaux, recalculés par l'évaluateur, sont justes : 27,7 %, 53,7 %, gain simulé de +5,4 points [+1,5 ; +9,2], intervalles à ±17 et ±10 points, parts de la liste d'audit. Points salués : grain et étoile, classement des KPI, nomenclatures réparées (zéro initial des CPV, lots inconnus distingués des non-allotis), seuils d'effectif différenciés, relation définitionnelle grisée « rien », arbitrage PME contre concurrence chiffré, navigation vérifiée.

La faiblesse principale tient en une phrase : **le dossier va plus loin en inférence que ce que ses propres résultats autorisent.** Corrections demandées, par priorité :

| Priorité | Sujet | Ce qui est reproché | Correction attendue |
| --- | --- | --- | --- |
| 1 | KPI 4, gain simulé | L'effet change de sens selon le pays (1,30 brut, 1,15 à valeur contrôlée, 1,06 avec le pays, inversé en DE et UK) : « causal plausible » est trop fort. Le gain applique à la France un rapport estimé sur tous les pays. Le rapport figé sous filtre affiche une précision fausse (par exemple sur les seuls services). Biais de sélection non discuté. DE et UK sans intervalle, contre la règle du bloc 4 de la vue 1 | Renommer le KPI (« écart ajusté » plutôt que « gain simulé »), le calculer par pays avec son intervalle, ne l'afficher que là où il a été estimé, parler d'« association ajustée, hétérogène » |
| 2 | Indice d'anomalie (KPI 6) | La strate CPV × type de contrat contrôle trop peu : avec 489 marchés pesant 36,6 % du montant, l'indice détecte surtout les plus gros contrats de chaque strate. La story 8 mélange les 489 marchés à z > 3 et l'audit de 5 % (7 460 marchés) | Ajouter au moins pays, année et classe de lots, idéalement un résidu de régression sur le logarithme du montant ; fixer quelle liste sert à l'audit |
| 3 | Chiffres de la note | 149 813 et 336 doublons, 6 022 lignes pour un fichier de 6 024, ne sont pas expliqués ensemble | Voir « Points à vérifier » : 336 = 334 dans le principal + 2 dans les rares si les deux fichiers sont dédoublonnés |
| 3 | Renvois au cours | « Erreur sanctionnée n° 15 » (deux fois) | L'empilement des deux fichiers est l'erreur sanctionnée **n° 11** |
| 3 | Valeur sentinelle | Le KPI 1 exclut 940, mais l'annexe cite des cas « jusqu'à 999 offres » | Dire si 999 est exclu ; les médianes y sont insensibles, pas les taux ni les effectifs |
| 3 | Code NOC | « Sens du code non confirmé », mais NOC classée définitionnelle et exclue du KPI 1 | Trancher, ou retirer le statut définitionnel |
| 3 | Montant pondéré (KPI 5) | L'échantillon reproduit mal la queue : chaque très gros marché est multiplié par environ 15 | Tester la part du Royaume-Uni sans le dernier centile avant de construire la story 12 dessus |
| 3 | « Prospectif » | La médiane et l'indice d'anomalie sont dits prospectifs ; la note écrit elle-même que la médiane est associée à l'offre unique « sans la précéder » | Seul le KPI 4 est avancé, sous les réserves ci-dessus |
| 3 | User stories | US1 contredit la vue 3 (tri par taux, alors que la vue 3 trie par valeur en jeu). US10 et US12 font manipuler le décideur, qui ne passe pas plus de 2 minutes dans l'outil. US7 est un contrôle de qualité, pas une décision | Réécrire US1, US7, US10 et US12 |
| 4 | Charge de construction | Six KPI dont un modèle logistique et des scores par strate : l'architecture la plus lourde | Préparer les deux calculs modélisés hors de l'outil et les importer comme colonnes |

## 4. Consigne de la séance 5 : construire l'application

**Objectif.** Transformer le plan (modèle, quatre vues, huit user stories) en application décisionnelle qui fonctionne, au service des pouvoirs publics, sur les trois axes. Le critère de réussite n'est pas l'apparence de l'écran : c'est la capacité de l'application à répondre correctement aux user stories, sur les trois axes, et à une question que l'équipe n'a pas prévue.

**Outil libre** (Looker Studio, Tableau Public, Streamlit, Lovable, artefact Claude, ou autre), à une condition non négociable : **URL publique, sans authentification.** Vérifier avant de construire :

- l'URL s'ouvre en navigation privée, depuis un autre poste ;
- l'outil recalcule à partir des lignes, pas d'agrégats figés ;
- l'outil supporte le volume (150 147 lignes) avec trois filtres croisés ;
- aucune clé, aucun identifiant dans le code ou les données publiées ;
- avec un outil génératif, chaque formule est relue et testée.

**Les six étapes.**

| Étape | Contenu |
| --- | --- |
| 1 · Couche de mesures | Avant le moindre graphique. Import propre (séparateur décimal point), deux sources distinctes jamais empilées, dédoublonnage de la séance 2. Chaque indicateur est un rapport d'agrégats : numérateur et dénominateur sont deux champs séparés, le quotient est recalculé à l'affichage. Effectif à côté du taux ; sous le seuil, indicateur masqué ou grisé avec mention de l'effectif. Contrôle sans filtre : retrouver les valeurs de contrôle du guide (taux de soumissionnaire unique, médiane des montants, part des PME parmi les renseignés), tout écart expliqué |
| 2 · Vue globale | Six indicateurs au plus, trois axes, effectif visible sans clic, périmètre écrit à l'écran (notamment la fenêtre de l'axe PME). Filtres de contexte uniquement, chacun relié à une user story. Au moins un indicateur avancé à côté des indicateurs de résultat |
| 3 · Vue segmentation | Croisements pays, secteur, procédure ; filtres croisés, tris multiples. Priorisation propre à chaque axe : A, segments classés par montant en jeu (pas par taux brut), paramètre réglable de capacité d'instruction N avec montant cumulé couvert, procédures sans mise en concurrence exclues ou signalées ; B, segments où l'allotissement est le plus faible et l'enjeu PME le plus fort, avec le taux de renseignement de la variable PME affiché ; C, segments dont les montants s'écartent de ce qu'annoncent leurs caractéristiques (contrat, secteur, procédure), grain d'attribution traité. Combiner trois filtres et vérifier l'affichage sous le seuil |
| 4 · Vue analyse | Pour chaque axe, au moins une relation de la séance 3 visible avec sa stratification par un confondant et les effectifs des deux groupes. L'utilisateur choisit la relation et active la stratification |
| 5 · Vue exploration | Descente jusqu'à la ligne par drill-down depuis les trois autres vues. Aucun écran mort : vérifier le schéma de navigation de la séance 4 dans l'application réelle |
| 6 · Recette | Exécuter les huit user stories : réussite ou échec, temps, cause de l'échec, correction. La story du décideur politique échoue au-delà de deux minutes. Puis un membre d'une autre équipe teste l'application sur une question qu'il formule lui-même. Une story impossible signale un filtre manquant, une mesure mal codée ou une story mal écrite : dire lequel |

**Livrables.**

| Livrable | Échéance | Contenu |
| --- | --- | --- |
| URL publique et fiche de paramétrage des mesures | 14/11, fin de séance | Pour chaque indicateur : formule implémentée, numérateur, dénominateur, effectif affiché, seuil, comportement sous le seuil, valeur de contrôle obtenue |
| Application complète | 20/11 | Quatre vues fonctionnelles couvrant les trois axes, filtres opérants, drill-down, effectifs affichés |
| Cahier de recette | 20/11 | Huit user stories testées : résultat, temps, cause d'échec, correction |
| Registre des écarts | 20/11, une demi-page | Ce qui a changé entre maquette et application, et pourquoi ; tout écart imposé par l'outil est signalé comme tel |
| Journal de bord | À chaque session de travail | Mis à jour y compris entre les séances |

**Grille (20 points).**

| Critère | Pts | Valorisé | Sanctionné |
| --- | --- | --- | --- |
| Exactitude des mesures | 4 | Indicateurs recalculés à chaque filtre, effectifs associés, valeurs de contrôle retrouvées ou écart expliqué | Moyenne de taux, somme non dédoublonnée, fichiers empilés |
| Vue globale | 3 | Six indicateurs au plus, trois axes couverts, périmètre affiché | Surcharge, pourcentage sans effectif, axe absent |
| Vue analyse | 4 | Une relation stratifiée par axe, effectifs visibles, aucune formulation causale abusive | Vue descriptive, absence de confondant, « X entraîne Y » sur une association |
| Vue segmentation | 4 | Priorisation par valeur, contrainte de ressource paramétrable, logique propre à chaque axe | Classement par taux brut, petits segments en tête, procédures non concurrentielles en tête |
| Exploration et navigation | 2 | Drill-down depuis les trois vues jusqu'à la ligne | Écran mort, exploration isolée |
| Recette et déploiement | 3 | URL publique fonctionnelle, temps de réponse acceptable, recette réelle et diagnostiquée | **URL inaccessible le 20/11 : 0 à l'ensemble du critère** |

**Pièges signalés.** Commencer par les graphiques ; faire générer l'application par une IA sans vérifier (recalculer à la main trois valeurs filtrées) ; traiter un axe et en oublier deux ; taux juste globalement mais faux filtré (tester chaque indicateur sur un pays et une année contre un calcul manuel) ; repousser les vues analyse et exploration au dernier soir ; abandonner la maquette au premier obstacle sans consigner l'écart ; accumuler des filtres (un filtre sans user story est retiré) ; tester l'URL uniquement depuis sa session ; recette complaisante (une story réussie en huit minutes pour le décideur est un échec).

**Connaissances à mobiliser.** Additivité des mesures (Kimball) ; architecture de l'information (Shneiderman, 1996) ; perception graphique (Cleveland et McGill, 1984) ; sémiologie graphique (Bertin, 1967) ; facteur de mensonge et rapport données-encre (Tufte, 1983) ; paradoxe de Simpson ; usage interactif (Simons, 1995) ; petits effectifs et classements (seuil d'effectif ou graphique en entonnoir, Spiegelhalter, 2005) ; règle d'affichage reconduite : tout pourcentage avec son effectif absolu, y compris après filtrage.

## 5. Plan d'action jusqu'au 20 novembre

Diagnostic confirmé du prototype : les 6 022 lignes des procédures rares y étaient embarquées et recalculées, mais tout le fichier principal (KPI, segments, relations, liste d'audit) était écrit en dur, et les filtres ne changeaient aucun chiffre. L'application `docs/index.html` recalcule désormais chaque indicateur à partir des 149 811 lignes à chaque filtre. État au 20 novembre :

### A. Bloquants, à traiter en premier

| # | Action | Pourquoi | Fait |
| --- | --- | --- | --- |
| A1 | Confirmer l'outil et l'URL publique : l'ouvrir en navigation privée, depuis un autre poste. Si le prototype HTML est conservé, le publier (par exemple GitHub Pages, le dépôt étant public). Ne pas utiliser Power BI sans validation écrite, et sans licence ni autorisation de publication sans authentification | URL inaccessible le 20/11 : 0 à tout le critère « Recette et déploiement » | [x] |
| A2 | Décider comment les mesures se recalculent. Option 1 : charger les lignes du fichier principal et calculer dans la page. Option 2 : un cube de comptages à granularité fine (pays × année × secteur × procédure × contrat × classes), dont numérateurs et dénominateurs s'additionnent exactement et dont le quotient est calculé à l'affichage. Les deux calculs modélisés (écart ajusté du KPI 4, indice d'anomalie) se préparent hors de l'outil et s'importent comme colonnes | La consigne interdit les agrégats figés ; un taux juste sans filtre et faux avec filtre est plus dangereux qu'une application vide | [x] |
| A3 | Confirmer l'état de la fiche de paramétrage des mesures, due le 14/11 | Livrable de fin de séance 5 | [x] |

### B. Couche de mesures (4 points)

- [x] Chaque indicateur est codé en numérateur, dénominateur et quotient séparés ; l'effectif s'affiche à côté ; seuil et comportement sous seuil appliqués (règles de la note de modélisation).
- [x] Valeurs de contrôle sans filtre retrouvées : taux de soumissionnaire unique, médiane des montants, part des PME parmi les renseignés. Tout écart est expliqué par le dédoublonnage ou le périmètre.
- [x] Trois valeurs filtrées recalculées à la main (un pays, une année) et comparées à l'écran, pour chaque indicateur.
- [x] Fiche de paramétrage à jour : formule, numérateur, dénominateur, effectif, seuil, comportement sous le seuil, valeur de contrôle obtenue.

### C. Les quatre vues (13 points)

- [x] **Vue 1 (3 pts)** : six indicateurs au plus, trois axes, effectif visible sans clic, périmètre affiché dont la fenêtre 2016-2017 ; chaque filtre relié à une user story ; au moins un indicateur avancé (voir la correction sur le mot « prospectif »).
- [x] **Vue 3 (4 pts)** : par axe, A en montant en jeu avec paramètre de capacité N et montant cumulé couvert, procédures sans concurrence exclues ou signalées ; B avec le taux de renseignement de la variable PME ; C avec la strate élargie. Combiner trois filtres et vérifier l'affichage sous le seuil.
- [x] **Vue 2 (4 pts)** : pour chacun des trois axes, au moins une relation stratifiée avec les effectifs des deux groupes ; aucune formulation causale abusive.
- [x] **Vue 4 (2 pts)** : drill-down jusqu'à la ligne depuis les trois autres vues ; schéma de navigation de la séance 4 vérifié dans l'application réelle.

### D. Corrections issues du retour (section 3)

- [x] Renommer et recalculer le KPI 4 par pays avec intervalle ; supprimer l'application d'un rapport figé sous filtre.
- [x] Élargir la strate de l'indice d'anomalie (pays, année, classe de lots, ou résidu de régression) ; fixer la liste qui sert à l'audit.
- [x] Corriger les chiffres (149 813 / 336 / 6 022), le renvoi « n° 15 » vers « n° 11 », le sort de la valeur 999, le statut de NOC.
- [x] Tester le montant pondéré sans le dernier centile avant de s'appuyer sur la story 12.
- [x] Réécrire les stories 1, 7, 10 et 12.

### E. Recette et dépôt (3 points)

- [x] Cahier de recette : huit stories, résultat, temps, cause d'échec, correction ; le décideur politique échoue au-delà de deux minutes. **Colonne « temps » à remplir au chronomètre par l'équipe.**
- [ ] Un membre d'une autre équipe teste l'application sur une question qu'il formule lui-même.
- [x] Registre des écarts (une demi-page) : ce qui a changé entre maquette et application, écarts imposés par l'outil signalés comme tels.
- [x] Journal de bord à jour.
- [ ] Test de l'URL en navigation privée, depuis un autre poste, la veille et le jour du dépôt.

### F. Après le 20 novembre

- [ ] Préparer la revue croisée de la séance 6 (l'application est auditée telle que livrée le 20).
- [ ] Reporter les corrections dans les documents des séances suivantes (recommandations, soutenance).

## 6. Consigne de la séance 4 (archive)

Objectif : produire un plan, pas un prototype, sans outil de visualisation. Trois étapes, trois livrables.

| Étape | Contenu | Livrable |
| --- | --- | --- |
| 1 · Modèle de données | Grain ; classement des six KPI (mesure, agrégat, indicateur) ; six dimensions (modalités, résiduelles, drill-down) ; trois règles transversales (seuil d'effectif, périmètre par défaut, répartition des deux fichiers) | Note de modélisation, 2 pages |
| 2 · Quatre vues | Globale (où en sommes-nous ?), Analyse (pourquoi ?), Segmentation (où agir ?), Exploration (quel cas précis ?), plus une feuille de navigation ; par bloc : indicateur, dénominateur, effectif minimal, visualisation, justification | 5 feuilles annotées |
| 3 · User stories | Huit stories au format « En tant que…, je veux…, afin de… » avec quatre champs ; deux par axe, trois profils, une story multi-vues | Un tableau |

Grille de la séance 4 : modèle et règles transversales (5), architecture des quatre vues (6), justification des encodages (4), user stories (5).

## 7. Contenu du dépôt

| Chemin | Contenu |
| --- | --- |
| `livrables/S4_BI_Livrable_Observatoire_marches_publics.docx` | Rendu 4 : note de modélisation, maquettes annotées, user stories, annexe « Pourquoi ces six KPI » |
| `Observatoire européen des marchés publics · Tableau de bord.html` | Prototype HTML du tableau de bord (vues 1 à 4), déposé sur `main` |
| `docs/superpowers/specs/2026-11-04-s4-architecture-dashboard-design.md` | Plan de travail de la séance 4 : intention, contraintes, méthode, arbitrages |
| `docs/index.html`, `docs/data/` | **Application publiée** (GitHub Pages, dossier `/docs`) et ses données : `principal.json`, `rares.json` (jamais empilés), `modeles.json` (KPI 4 par pays) |
| `scripts/prepare_data.py` | Préparation des données depuis les fichiers FINAL : dédoublonnage, sentinelles, indice d'anomalie (résidu de régression), KPI 4 par pays |
| `scripts/reference.py` | Calcul de référence indépendant des KPI et de la vue 3, qui sert d'arbitre pour chaque valeur affichée |
| `livrables/S5_cahier_de_recette.md` | Cahier de recette : 8 stories, résultats, diagnostics, corrections ; grille du test par une autre équipe |
| `livrables/S5_fiche_parametrage_mesures.md` | Fiche de paramétrage : formule, numérateur, dénominateur, effectif, seuil, comportement sous le seuil, valeur de contrôle |
| `livrables/S5_registre_des_ecarts.md` | Registre des écarts maquette → application (demi-page, détail en annexe) |
| `livrables/S5_journal_de_bord.md` | Journal de bord des sessions de travail |
| `livrables/S5_pitch.md` | Pitch de 90 secondes et réponses prêtes aux questions probables |
| `livrables/S5_guide_stories_pas_a_pas.md` | Pas-à-pas des 8 stories à suivre chronomètre en main (moins de 10 minutes au total) |
| `README.md` | Ce fichier |

## 8. Décisions clés

**Les six KPI**, deux par axe : l'état, puis le levier ou le ciblage. KPI 4 et indice d'anomalie corrigés en séance 5 (section 3).

| Axe | KPI | Type | Lien qui le fonde | Action déclenchée |
| --- | --- | --- | --- | --- |
| A | 1 · Taux d'offre unique, procédure ouverte | indicateur | associatif | entre dans les 20 dossiers |
| A | 2 · Médiane des offres | agrégat non additif | associatif faible | liste de surveillance |
| B | 3 · Part de PME, 2016-2017 | indicateur | associatif | revue d'allotissement |
| B | 4 · Écart ajusté du 6-10 lots, par pays (France +8,8 pts [+1,1 ; +16,5]) | indicateur avancé (estimé hors de l'outil) | association ajustée, hétérogène | pilote encadré en France, seul pays où l'association est établie |
| C | 5 · Montant total pondéré | agrégat additif | descriptif | vérifier la queue avant l'audit |
| C | 6 · Indice d'anomalie (résidu de régression, z robuste) | mesure stockée par ligne | associatif | liste d'audit unique de N attributions |

**Grain.** Une ligne est une attribution (ID_AW), dans le fichier principal dédoublonné.

**Trois règles transversales.**

1. Seuil d'effectif par KPI : 100 marchés pour les KPI 1 à 3, 100 non-allotis pour le KPI 4, 30 attributions pour le KPI 5, 30 marchés par strate pour le KPI 6. Sous le seuil, la case affiche « effectif insuffisant ».
2. Périmètre par défaut : fichier principal ; procédure ouverte pour les KPI 1 et 2 ; fenêtre 2016-2017 verrouillée pour les KPI 3 et 4, qui ignorent le filtre d'année global.
3. Deux fichiers : le principal alimente les vues 1 à 3 ; les procédures rares n'apparaissent qu'en vue 4, lues procédure par procédure, sans jamais être additionnées (erreur sanctionnée n° 11 du cours).

**Un seul lien survit au contrôle des confondants** : le passage à 6-10 lots et la part de PME (R3), et il reste fragile (inversé en Allemagne et au Royaume-Uni). Les autres relations servent à cibler et à surveiller, pas à recommander.

## 9. Points à vérifier dans les données

Les chiffres des documents viennent de la note de la séance 3 ; l'évaluateur a recalculé les principaux, qui sont justes.

- ✅ **Effectifs.** Confirmé par les journaux des fichiers FINAL : 334 doublons dans le principal (150 147 → 149 813) et 2 dans les rares (6 024 → 6 022). Écrit dans l'application (onglet Mesures) et le registre (E5).
- ✅ **Valeur 999.** 3 lignes (Bulgarie, 2014, même acheteur, 45 lots), mises à vide comme 940 (registre E4). **ID_AW 164662498** présent 3 fois : une seule ligne gardée (E3).
- ✅ **Code NOC.** Statut définitionnel retiré ; NOC reste exclue du KPI 1 par précaution (E21). **Médiane du KPI 2** : écrite « associée à » l'offre unique (E14).
- Bornes exactes des classes de valeur et de lots (règle 11 du nettoyage) et nombre de divisions CPV.
- Les deux modalités sans information du type d'acheteur, regroupées en « Non précisé ».
- Dénominateurs de la part des pays dans la liste d'audit : 149 813 pour le Royaume-Uni, 149 218 pour la Pologne.
- Le suivi de la recommandation est annuel : le fichier n'a pas de donnée infra-annuelle.
