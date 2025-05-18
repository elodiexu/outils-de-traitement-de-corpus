import os
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_name = "plguillou/t5-base-fr-sum-cnndm"

print(" Chargement du modèle...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
paraphraser = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

csv_path = os.path.join("..", "..", "data", "raw", "all_comments.csv")
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Fichier introuvable : {csv_path}")

df = pd.read_csv(csv_path)

augmented_data = []

print("🪄 Génération des paraphrases...")
for i, row in df.iterrows():
    original = str(row["comment"])

    try:
        prompt = "resumer: " + original 
        output = paraphraser(prompt, max_length=128, num_return_sequences=1, do_sample=True)
        rewritten = output[0]["generated_text"]

        augmented_data.append({
            "film": row["film"],
            "year": row["year"],
            "original_comment": original,
            "augmented_comment": rewritten
        })

    except Exception as e:
        print(f" Erreur sur ligne {i}: {e}")
        continue

output_dir = os.path.join("..", "..", "data", "clean")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "paraphrased_comments.csv")

aug_df = pd.DataFrame(augmented_data)
aug_df.to_csv(output_path, index=False, encoding="utf-8")

print(f" Fichier généré : {output_path}")