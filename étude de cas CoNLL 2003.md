###Partie 1 | étude de cas CoNLL 2003 :   
1. Quelle type de tâche propose CoNLL-2003 ?   
	CoNLL-2003 propose une tâche de reconnaissance d’entités nommées (NER - Named Entity Recognition). L’objectif est d’identifier et de classifier des entités spécifiques dans un texte, telles que les noms de personnes, les lieux, les organisations et d’autres entités diverses.   
	
2. Quel type de données y a-t-il dans CoNLL-2003 ?   
	- Type de données : Texte   
	- Intention du dataset : Ce dataset est introduit lors de la conférence de 2003 de Natural Language Learning. CoNLL signifie Conference on Natural Language Learning. C’est le premier jeu de données majeur introduit pour faire de la NER.   
	- Langues : Anglais, Allemand   

3. À quel besoin répond CoNLL-2003 ?   
	CoNLL-2003 répond aux besoins de traitement automatique des langues, en particulier pour :   
	- L’amélioration des modèles de reconnaissance d’entités nommées (NER).   
	- L’entraînement et l’évaluation de modèles supervisés de NLP.   
	- L’analyse de texte et l’extraction d’information à partir de documents.   

4. Quels types de modèles ont été entraînés sur CoNLL-2003 ?      
Différents modèles ont été entraînés sur CoNLL-2003 :   
	- 	Méthodes traditionnelles :    
	a. CRF (Conditional Random Fields) : Modèle probabiliste pour l’étiquetage de séquence.     
	b. HMM (Hidden Markov Model) : Modèle statistique basé sur des transitions entre états.     
	- 	Méthodes basées sur le Deep Learning :    
	a. BiLSTM-CRF : Un réseau de neurones récurrent (LSTM) bidirectionnel combiné avec CRF.   
	b. BERT + CRF : Modèles basés sur les Transformers, comme BERT, RoBERTa, XLM-R, fine-tunés sur CoNLL-2003.    
	
5. Est-ce un corpus monolingue ou multilingue ?   
	CoNLL-2003 est un corpus multilingue, car il contient des données en Anglais et Allemand.
