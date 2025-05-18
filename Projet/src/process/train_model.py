import pandas as pd
from datasets import Dataset
from transformers import CamembertTokenizer, CamembertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../data/clean/paraphrased_comments.csv")
label_map = {"négatif": 0, "neutre": 1, "positif": 2}
df["label"] = df["label"].map(label_map)
df1 = df[["original_comment", "label"]].rename(columns={"original_comment": "text"})
df2 = df[["augmented_comment", "label"]].rename(columns={"augmented_comment": "text"})
df = pd.concat([df1, df2], ignore_index=True).dropna()

tokenizer = CamembertTokenizer.from_pretrained("camembert-base")

def tokenize_function(example):
    return tokenizer(example["text"], padding="max_length", truncation=True)

dataset = Dataset.from_pandas(df)
tokenized_dataset = dataset.map(tokenize_function, batched=True)

split = tokenized_dataset.train_test_split(test_size=0.2)
train_dataset = split["train"]
eval_dataset = split["test"]

model = CamembertForSequenceClassification.from_pretrained("camembert-base", num_labels=3)

training_args = TrainingArguments(
    output_dir="../../bin/camembert-finetuned",
    eval_strategy="epoch" ,
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=4,
    weight_decay=0.01,
    logging_dir="../../logs",
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

trainer.train()