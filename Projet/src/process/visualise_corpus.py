import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os
import re
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stopwords_fr = set(stopwords.words("french"))

csv_path = os.path.join("..", "..", "data", "raw", "all_comments.csv")

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"fichier non trouvé")

df = pd.read_csv(csv_path)

def clean_text(text):
    text = str(text).lower()
    return re.sub(r"[^\w\s]", "", text)

def remove_stopwords(text):
    words = text.split()
    return " ".join([w for w in words if w not in stopwords_fr])

df["clean_comment"] = df["comment"].apply(clean_text)
df["no_stopwords"] = df["clean_comment"].apply(remove_stopwords)
df["comment_length"] = df["clean_comment"].apply(lambda x: len(x.split()))
all_words = " ".join(df["no_stopwords"]).split()
word_counts = Counter(all_words)
most_common_words = word_counts.most_common(30)

figures_path = os.path.join("..", "..", "figures")
os.makedirs(figures_path, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.hist(df["comment_length"], bins=20, color='lightcoral', edgecolor='black')
plt.title("Distribution de la longueur des commentaires")
plt.xlabel("Nombre de mots")
plt.ylabel("Nombre de commentaires")
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "comment_length_distribution.png"))
plt.close()

ranks = np.arange(1, len(most_common_words) + 1)
frequencies = [count for word, count in most_common_words]
labels = [word for word, count in most_common_words]

plt.figure(figsize=(10, 5))
plt.plot(ranks, frequencies, marker='o')
plt.xticks(ranks, labels, rotation=45, ha='right')
plt.title("Loi de Zipf : mots les plus fréquents")
plt.xlabel("Rang")
plt.ylabel("Fréquence")
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "zipf_most_common_words.png"))
plt.close()

print("Graphiques et statistiques générés avec succès ! Résultats dans les dossiers figures/")