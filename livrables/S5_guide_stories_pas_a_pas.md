# Pas-à-pas des 8 user stories (à suivre chronomètre en main)

Durée totale visée : **moins de 10 minutes** pour les 8 stories. Reporter chaque temps dans la colonne « Temps » du cahier de recette.

## Avant de commencer (1 minute)

1. Ouvrir une **fenêtre de navigation privée** (Chrome : Ctrl + Maj + N ; Safari : Cmd + Maj + N).
2. Aller sur **https://amandacatarinoac-cmd.github.io/exobusinessintelligence/** et attendre les six cartes de la vue 1 (environ 1 seconde).
3. **Entre deux stories** : recoller l'adresse de départ, sans le « #… » de fin, puis Entrée. Tous les filtres et réglages reviennent à zéro et la vue 1 s'ouvre.
4. Le chronomètre démarre quand on commence à lire l'écran et s'arrête quand on peut **dire la décision à voix haute**.

## Les stories

### Story 10 · Décideur politique · choisir l'axe à porter à l'arbitrage · objectif < 2 min
- **Clics** : aucun. Rester sur la vue 1.
- **Lire** : les six cartes, leur valeur, leur effectif sous la valeur et leur badge.
- **Réponse attendue** : la seule alerte orange est sur le KPI 5 : « 69 % porté par 1 % des montants ». **Décision : porter l'axe C (budget) à l'arbitrage.**

### Story 5 · Décideur politique · lancer ou non le 6-10 lots · objectif < 2 min
- **Clics** : aucun. Vue 1, carte 4.
- **Lire** : « France +8,8 pts », « IC 95 % [1,1 ; 16,5] », le petit graphique (Allemagne et Royaume-Uni en point creux), puis l'encadré « Prix à payer (R2) » : +10,4 points d'offre unique.
- **Réponse attendue** : association établie en France seulement, imprécise, avec un coût en offre unique. **Décision : pas de généralisation ; au mieux un pilote en France avec condition d'arrêt.**

### Story 1 · Responsable de la surveillance · les dossiers à instruire · objectif < 1 min
- **Clics** : 1. Onglet **3 · Segmentation** (l'axe A est ouvert par défaut).
- **Lire** : la rangée de chiffres : 21 segments en alerte, 20 dossiers retenus, 36,09 Md€ couverts ; puis le haut du tableau : Pologne × 33 « Instruire », 17,47 Md€.
- **Réponse attendue** : **instruire les 20 segments marqués « Instruire », dans l'ordre du montant en jeu.**

### Story 2 · Responsable de la surveillance · la liste de surveillance · objectif < 1 min
- **Clics** : 2. Onglet **3 · Segmentation** → bouton **Afficher : Surveillance**.
- **Lire** : 26 segments, sous la ligne « 26 segments avec ce statut, tous affichés ».
- **Réponse attendue** : **inscrire ces 26 segments en liste de surveillance** (en tête : Pologne × 90).

### Story 4 · Responsable de la surveillance · revue d'allotissement · objectif < 1 min 30
- **Clics** : 1. Vue 1, carte 3 → lien **« Où agir ? pays sous 40 % → »**.
- **Lire** : 4 pays marqués « Revue d'allotissement » ; colonne « Taux de renseignement » : Espagne 32 %, Italie 32 %, Autriche 72 %, Norvège 44 %.
- **Réponse attendue** : **ouvrir la revue d'abord en Autriche** ; pour les trois autres, faire d'abord vérifier le renseignement de la variable PME.

### Story 3 · Analyste · où l'enchère électronique a un fondement · objectif < 1 min 30
- **Clics** : 1. Onglet **2 · Analyse** (R1 et la stratification par pays sont ouvertes par défaut).
- **Lire** : la phrase de lecture (« association hétérogène »), puis le tableau : Pologne 0,40, Tchéquie 0,12 en point plein ; France 1,37 en point creux ; Italie 1,95 en sens inverse.
- **Réponse attendue** : **promouvoir l'enchère en Pologne, Tchéquie et Hongrie** (la Hongrie, 0,16, est plus bas dans le tableau) ; **ne pas l'imposer en France ni en Italie.**

### Story 8 · Responsable de la surveillance · constituer la liste d'audit · objectif < 1 min 30
- **Clics** : 3. Onglet **3 · Segmentation** → **C · Budget** → lien **« Voir toute la liste d'audit → »**.
- **Lire** : « 500 attributions » en vue 4, triées par indice d'anomalie ; en tête l'ID_AW 115005289 (354,7 M€ pour 4 126 € attendus).
- **Option (+1 clic)** : filtre **Type de contrat** pour lire la liste par contrat (Travaux : 34 attributions).
- **Réponse attendue** : **la liste d'audit est constituée** ; cliquer une ligne ouvre sa fiche pour retenir ou écarter le dossier.

### Story 12 · Analyste · répartir ou non l'audit par pays · objectif < 1 min 30
- **Clics** : 2. Onglet **3 · Segmentation** → **C · Budget**.
- **Lire** : le tableau « Liste d'audit : qui y pèse ? » : Royaume-Uni 16,6 % de la liste pour 3,5 % des attributions, 42,3 % du montant mais **11,0 % sans le dernier centile** ; Lettonie 18,2 % de la liste pour 2,6 % des attributions.
- **Réponse attendue** : **pas de quota par pays fondé sur le montant** ; examiner d'abord la Lettonie.

## Si une story échoue

Noter dans le cahier, colonne « Cause de l'échec », l'une des trois causes prévues par la consigne :
- **filtre manquant** : on ne peut pas isoler ce qu'il faut ;
- **mesure mal codée** : le chiffre ne correspond pas au calcul de référence ;
- **story mal écrite** : la décision demandée n'est pas celle que l'écran permet de prendre.
Pour le décideur (stories 5 et 10), **au-delà de 2 minutes, c'est un échec**, même si la réponse est juste.

## Pour le test par une autre équipe

Laisser le testeur formuler sa question sans l'aider. Noter sa question, son chemin, son temps et la réponse obtenue dans la section 4 du cahier de recette. Si l'application répond « effectif insuffisant », c'est une réussite : elle refuse de publier un chiffre fragile.
