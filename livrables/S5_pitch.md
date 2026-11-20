# Pitch · application décisionnelle (environ 90 secondes)

À dire en ouvrant l'application sur la vue 1 : https://amandacatarinoac-cmd.github.io/exobusinessintelligence/

---

**[0-15 s] Le problème.**
« La Commission doit préparer la surveillance 2018 des marchés publics. Notre application ne décrit pas le marché : elle aide à décider **où agir**, sur trois axes : la concurrence, l'accès des PME, la dépense anormale. »

**[15-35 s] La règle qui commande tout.**
« Chaque chiffre est recalculé à partir des 149 811 attributions, à chaque filtre. Jamais une moyenne de taux. Chaque taux s'affiche avec son numérateur et son dénominateur ; sous le seuil d'effectif, l'application écrit "effectif insuffisant" au lieu de publier un chiffre fragile. Nous avons vérifié trois sélections filtrées contre un calcul fait directement sur le fichier Excel : tout concorde. »

**[35-65 s] Trois décisions que l'outil rend possibles.**
« Axe A : avec une capacité de 20 dossiers, on instruit les segments classés par **montant en jeu**, pas par taux. Ces 20 dossiers couvrent 36 milliards d'euros de dépense à offre unique, en tête la Pologne en matériel médical.
Axe B : quatre pays sont sous 40 % de PME, mais trois sont trop mal renseignés pour conclure. On commence donc par l'Autriche.
Axe C : 1 % des montants porte 69 % de la dépense. Une seule liste d'audit de 500 attributions couvre 28 % du montant ; la première est un marché de 355 millions d'euros quand le montant attendu est de 4 000 euros. »

**[65-85 s] Ce que nous ne disons pas.**
« Le découpage en 6 à 10 lots va avec plus de PME en France, + 8,8 points, mais l'intervalle va de + 1 à + 16 points, l'effet s'inverse en Allemagne et au Royaume-Uni, et il coûte des offres uniques. C'est une association, pas une cause : nous proposons au mieux un pilote en France, avec une condition d'arrêt. »

**[85-90 s] L'invitation.**
« Posez-nous une question que nous n'avons pas prévue : l'application doit y répondre. »

---

## Réponses prêtes aux questions probables

| Question | Réponse courte |
|---|---|
| Pourquoi ne pas additionner les deux fichiers ? | Les procédures rares sont surreprésentées par construction : les additionner fausse tout taux (erreur sanctionnée n° 11). Elles sont lues à part, en vue 4, procédure par procédure, sans total. |
| Vos chiffres diffèrent de la note de la séance 3 ? | De quelques unités seulement : nous avons retiré deux copies d'une attribution présente trois fois et la valeur 999. Les taux ne bougent pas (27,7 % ; 53,7 %). Chaque écart est dans le registre. |
| Pourquoi le KPI 4 n'apparaît-il pas quand je filtre sur les services ? | Il a été estimé par pays, pas par contrat. Afficher un chiffre serait une précision fausse ; l'application l'écrit. |
| Pourquoi 40 % ? | C'est le seuil du cours ; la sensibilité est visible en vue 3 : 41, 21 et 7 segments en alerte à 30, 40 et 50 %. |
| Votre indice d'anomalie détecte-t-il des fraudes ? | Non. Il repère les montants très éloignés de ce qu'annoncent leurs caractéristiques. La fiche de la vue 4 permet de trancher : gros lot légitime, erreur de saisie ou dossier à auditer. |
| Le Royaume-Uni pèse 42 % du montant : faut-il un quota par pays ? | Sans le dernier centile, il ne pèse plus que 11 % : son poids tient à quelques très gros marchés. Pas de quota fondé sur le montant ; la Lettonie, surreprésentée dans la liste, est à examiner d'abord. |
