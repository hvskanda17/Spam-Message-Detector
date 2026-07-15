# Spam Message Detector

## Overview

Spam Message Detector is a machine learning web application developed to classify text messages as **Spam** or **Ham (Not Spam)**. The project combines a React.js frontend with a Python Flask backend, allowing users to enter a message and receive an instant prediction from a trained machine learning model.

The objective of this project is to demonstrate how machine learning can be integrated with a modern web application to solve a real-world problem such as spam message filtering.

---

## Features

* Classifies SMS messages as Spam or Ham
* Interactive and user-friendly React interface
* Flask API for handling prediction requests
* Machine learning model trained on SMS data
* Fast prediction response

---

## Technologies Used

### Frontend

* React.js
* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* TF-IDF Vectorizer
* Multinomial Naive Bayes

---

## Project Structure

```text
Spam-Message-Detector
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── backend
│   ├── app.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   ├── requirements.txt
│   └── ...
│
├── .gitignore
└── README.md
```

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/hvskanda17/Spam-Message-Detector.git
cd Spam-Message-Detector
```

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

Open another terminal.

```bash
cd frontend
npm install
npm start
```

---

## How the Application Works

1. The user enters a text message through the React application.
2. The message is sent to the Flask backend.
3. The backend preprocesses the text and converts it into numerical features using a TF-IDF vectorizer.
4. The trained machine learning model predicts whether the message is Spam or Ham.
5. The result is sent back to the frontend and displayed to the user.

---

## Future Enhancements

* Email spam detection
* Confidence score for predictions
* User authentication
* Prediction history
* Cloud deployment

---

## Author

**H V Skanda**

This project was developed as part of a Machine Learning academic project to demonstrate the integration of machine learning models with a full-stack web application.
