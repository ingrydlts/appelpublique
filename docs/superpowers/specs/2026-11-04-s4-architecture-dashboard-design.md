# S4 BI — Architecture décisionnelle du dashboard : design

Projet fil rouge : Observatoire européen des marchés publics (PSB, M2, BI, Dashboards & Data Storytelling).
Auteure : Ingryd Lo Tierzo Silva. Date : 4 novembre 2026.

## 1. Intention

Produire les trois livrables de la séance 4 (plan, pas prototype) en prolongement
direct de la séance 3 (six KPI, carte causale, recommandation 6-10 lots) :

1. tableau de **user stories** (minimum 8, cible 12 à 15) ;
2. **maquettes annotées** : 4 vues + schéma de navigation ;
3. **note de modélisation** (2 pages) : grain, classement des 6 KPI, dimensions, 3 règles transversales.

Le dépôt documente les décisions clés et sert de README. Aucun outil de visualisation :
la maquette est faite à la main / Word / PowerPoint, ce dépôt fournit le contenu à reprendre.

## 2. Contraintes tirées de la consigne et de la séance

- Ordre de travail demandé par le professeur : user stories → maquettes → modèle de données.
- Chaque KPI couvert par au moins une story ; 3 profils (responsable de la surveillance,
  analyste de l'Observatoire, décideur politique) ; au moins une story traversant plusieurs vues ;
  2 stories par axe (A concurrence, B PME, C budget) au minimum.
- Chaque story finit sur une **décision** (« afin de mieux comprendre » interdit).
- Vue 2 = une relation testée + stratification par un confondant + effectifs ; jamais un clone de la vue 1.
- Tout pourcentage est accompagné de son effectif.
- Prolonger la carte causale : pas d'indicateur « de remplissage ».
- Lacune relevée par le professeur : démontrer **pourquoi ces 6 KPI** et pas d'autres.
- Préciser « exclure » : cellule ou ligne ?
- L'auteure doit pouvoir défendre chaque choix : rien n'est figé sans validation de sa part.

## 3. Structure du dépôt

```
README.md
docs/01-kpi-et-carte-causale.md   synthèse des 6 KPI + démonstration du choix
docs/02-user-stories.md
docs/03-maquettes/                une fiche par vue, navigation, schémas SVG à redessiner
docs/04-modele-donnees.md         grain, classification, dimensions, 3 règles transversales
docs/05-decisions.md              journal : décision / pourquoi / « si on vous demande »
```

## 4. Méthode

- Je rédige chaque pièce avec ses justifications ; les arbitrages sont marqués **À décider**.
- Validation par l'auteure pièce par pièce avant commit du document final.
- Ordre : 02 → 03 → 04 → 01, README et 05 en continu.

## 5. Arbitrages ouverts (à trancher par l'auteure)

- Seuil d'effectif : une règle unique (100 ?) ou un seuil par KPI justifié (aujourd'hui 100 pour les KPI 1-4, 30 pour les KPI 5-6).
- Nombre de vues : 4 (imposé par la consigne écrite) ou davantage (toléré à l'oral).
- Fenêtre 2016-2017 des KPI 3 et 4 face au filtre d'année global.
- Classement du KPI 2 (médiane) et du KPI 6 (z-score à strate figée), KPI 4 (simulé, paramètre fixe).
- KPI à ajouter éventuellement (le professeur a dit que d'autres pouvaient manquer).

## 6. Hors périmètre

- Déploiement (Power BI, etc.) : séance suivante.
- Transcription de l'audio du cours, contenu Notion privé, données brutes : non versionnés.
- Aucun chiffre nouveau : tous les chiffres viennent du livrable de la séance 3 et sont à re-vérifier avant la défense.
