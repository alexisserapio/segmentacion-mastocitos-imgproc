# src/clasificador.py

import pickle
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

def train_svm(X_train, y_train):
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(f"Precisión global: {accuracy_score(y_test, y_pred):.2f}")

def save_model(model, path):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
