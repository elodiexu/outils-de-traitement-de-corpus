import pandas as pd
from datasets import Dataset
from transformers import CamembertTokenizer, CamembertForSequenceClassification, Trainer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, f1_score
import numpy as np

df = pd.read_csv("../../data/clean/paraphrased_comments.csv")
label_map = {"négatif": 0, "neutre": 1, "positif": 2}
df["label"] = df["label"].map(label_map)

df1 = df[["original_comment", "label"]].rename(columns={"original_comment": "text"})
df2 = df[["augmented_comment", "label"]].rename(columns={"augmented_comment": "text"})
df = pd.concat([df1, df2], ignore_index=True).dropna()
df = df[df["text"].str.strip() != ""]

_, test_df = train_test_split(df, test_size=0.2, random_state=42)

tokenizer = CamembertTokenizer.from_pretrained("camembert-base")

def tokenize_function(example):
    return tokenizer(example["text"], padding="max_length", truncation=True)

test_dataset = Dataset.from_pandas(test_df)
tokenized_test = test_dataset.map(tokenize_function, batched=True)

model = CamembertForSequenceClassification.from_pretrained("../../bin/camembert-finetuned/checkpoint-120")
trainer = Trainer(model=model)

predictions = trainer.predict(tokenized_test)
y_true = predictions.label_ids
y_pred = np.argmax(predictions.predictions, axis=1)

print(" Rapport de classification :\n")
print(classification_report(y_true, y_pred, target_names=["négatif", "neutre", "positif"]))
print(" Accuracy:", accuracy_score(y_true, y_pred))
print(" F1 (macro):", f1_score(y_true, y_pred, average='macro'))

test_df["predicted_label"] = y_pred
inv_label_map = {0: "négatif", 1: "neutre", 2: "positif"}
test_df["predicted_label_str"] = test_df["predicted_label"].map(inv_label_map)
test_df["true_label_str"] = test_df["label"].map(inv_label_map)
test_df.to_csv("../../data/clean/eval_predictions.csv", index=False)
print(" Résultats enregistrés dans data/clean/eval_predictions.csv")