import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_and_evaluate(X_text, y):
    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X_text)

    # Split into train and test data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Logistic Regression model
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluation results
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return model, vectorizer, X_train, X_test, y_train, y_test, accuracy, report


def save_model(model, vectorizer):
    with open("model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)

    with open("vectorizer.pkl", "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    print("\nModel and vectorizer saved successfully!")