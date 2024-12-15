# Import libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

model = load_model('ai-model.h5')

file_path = "https://raw.githubusercontent.com/ajisakarsyi/ai-project/refs/heads/main/ai-dataset/Data_Tanaman_Padi_Sumatera_version_1.csv" 
data = pd.read_csv(file_path)

columns = ['Luas Panen', 'Curah hujan', 'Kelembapan', 'Suhu rata-rata']
data_subset = data[columns]

feature_means = data_subset.mean().values
feature_stds = data_subset.std().values

scaler = StandardScaler()
scaler.mean_ = feature_means
scaler.scale_ = feature_stds

def preprocess_input(features):
    return scaler.transform([features])

def predict():
    print("Enter the following features for prediction:")
    try:
        luas_panen = float(input("Luas Panen: "))
        curah_hujan = float(input("Curah Hujan: "))
        kelembapan = float(input("Kelembapan: "))
        suhu_rata_rata = float(input("Suhu Rata-rata: "))
        
        features = [luas_panen, curah_hujan, kelembapan, suhu_rata_rata]
        processed_features = preprocess_input(features)
        
        prediction = model.predict(processed_features)
        print(f"Predicted Produksi: {prediction[0][0]:.2f}")
    except Exception as e:
        print(f"Error during prediction: {e}")

if __name__ == "__main__":
    predict()
