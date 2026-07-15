import pandas as pd
from preprocess import preprocess
from model_utils import train_and_evaluate, save_model

# Load dataset
df = pd.read_csv("spam.tsv", sep="\t", header=None, names=["label", "message"])

# Remove duplicates
df = df.drop_duplicates()

# Convert labels
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Apply preprocessing
df["message"] = df["message"].apply(preprocess)

# Features and labels
X_text = df["message"]
y = df["label"]

# Train and evaluate model
model, vectorizer, X_train, X_test, y_train, y_test, accuracy, report = train_and_evaluate(X_text, y)

# Save model files
save_model(model, vectorizer)

# Print results
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(report)