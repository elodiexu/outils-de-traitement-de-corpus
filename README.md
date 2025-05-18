## Project: Analyse des sentiments dans les critiques de films populaires (2022–2024)

- **Définissez les besoins de votre projet :**   
  Ce projet répond au besoin d’analyser automatiquement les sentiments exprimés dans les critiques de films.   
  Il vise à développer un outil de classification automatique capable de distinguer les opinions positives, neutres ou négatives à partir des critiques spectateurs en langue française.   
  Cela permettrait d’exploiter un grand volume de données issues du web (ici Allociné) pour mieux comprendre la réception des films populaires entre 2022 et 2024.   

- **dans quel besoin vous inscrivez-vous ?**   
  Je m’inscris dans le besoin d’automatiser l’analyse d’opinions dans le domaine du cinéma, en utilisant des techniques de traitement automatique des langues (TAL).   
Cela permet d’identifier les tendances générales du public sans passer par une lecture manuelle fastidieuse des commentaires.

- **quel sujet allez-vous traiter ?**   
  Je vais traiter le sujet suivant :  
  “Comment classifier automatiquement les critiques spectateurs des films populaires (2022–2024) selon leur polarité émotionnelle ?”

- **quel type de tâche allez-vous réaliser ?**   
  La tâche principale consiste à classifier automatiquement des critiques spectateurs selon leur polarité :   
	•	Création d’un corpus annoté (positif / négatif / neutre)    
	•	Entraînement d’un modèle de classification (CamemBERT)   
	•	Évaluation des performances et visualisation des résultats   

- **quel type de données allez-vous exploiter ?**   
  Je vais exploiter des données textuelles non structurées, à savoir des critiques spectateurs en langue française extraites du site Allociné.   
Elles sont ensuite organisées dans un fichier CSV, contenant les colonnes suivantes : film, année, commentaire original, commentaire augmenté, étiquette de polarité (positif, négatif, neutre).

- **où allez-vous récupérer vos données ?**   
  Sur le site **Allociné.fr**, en ciblant les **10 films les plus populaires** de chaque année : 2022, 2023 et 2024.

- **sont-elles libres d'accès ?**   
  Oui, les données sont **publiquement accessibles** sur le site Allociné dans le cadre d’une utilisation non commerciale et académique.
