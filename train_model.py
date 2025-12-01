import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Function to load and preprocess the data
def load_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    # Perform preprocessing such as handling missing values or categorical encoding
    data.fillna(data.mean(), inplace=True)  # Example: Fill missing values with mean
    # Encode categorical features if necessary
    # data = pd.get_dummies(data)
    
    return data

# Function to train a Random Forest model
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Function to visualize results
def visualize_results(y_true, y_pred):
    plt.figure(figsize=(10, 6))
    sns.heatmap(confusion_matrix(y_true, y_pred), annot=True, fmt='d')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
    print(classification_report(y_true, y_pred))

if __name__ == "__main__":
    # File path to your dataset
    file_path = 'data/construction_data.csv'  # Example file path
    data = load_data(file_path)
    
    # Assuming the target variable is 'target'
    X = data.drop('target', axis=1)
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)
    
    visualize_results(y_test, y_pred)