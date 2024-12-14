# Prediksi Produksi Padi Berdasarkan Data Cuaca

Proyek ini menggunakan model **Neural Network** berbasis **TensorFlow** untuk memprediksi jumlah produksi padi berdasarkan informasi cuaca dan luas panen. Dataset yang digunakan mencakup data tanaman padi dari **Sumatera**.

## 🚀 Fitur Utama

### 1. Prediksi Produksi Padi
- **Input**: Luas panen, curah hujan, kelembapan, dan suhu rata-rata.
- **Output**: Prediksi jumlah produksi padi dalam ton.

### 2. Klasifikasi Produksi
Hasil prediksi dikelompokkan ke dalam 4 kategori:
- **Produksi Rendah**
- **Produksi Sedang**
- **Produksi Tinggi**
- **Produksi Sangat Tinggi**

### 3. Arsitektur Neural Network
Jaringan terdiri dari beberapa lapisan **dense** dengan **dropout** untuk meningkatkan akurasi dan mengurangi overfitting.

---

## 🛠️ Langkah-Langkah Penggunaan

### 1. Prasyarat
Pastikan Anda telah menginstal pustaka yang diperlukan. Semua pustaka telah disediakan dalam file `requirements.txt`.

**Instal pustaka yang diperlukan dengan perintah berikut:**
```bash
pip install -r requirements.txt
```

### 2. Jalankan Model
1. **Unduh atau klon repositori ini**.
2. **Buka file** `ai-jupyter.ipynb`.
3. Ubah section input sesuai dengan luas panen, curah hujan, kelembapan, dan suhu rata-rata yang diinginkan.

### 3. Contoh Input dan Output

**Input**:
```python
luas_panen = 2000       # Luas panen (hektar)
curah_hujan = 150       # Curah hujan (mm)
kelembapan = 85         # Kelembapan (%)
suhu_rata_rata = 27     # Suhu rata-rata (°C)
```

**Output**:
```bash
Predicted Production: 800.34
Production Cluster: Produksi Rendah
```

---

## 📂 Struktur Proyek
- **`ai-jupyter.ipynb`**: Script utama untuk pelatihan model dan prediksi.
- **`ai-dataset`**: Dataset tanaman padi yang diambil dari sumber online.
- **`requirements.txt`**: Daftar pustaka yang diperlukan untuk menjalankan proyek.

---

## 📊 Detail Model
- **Input**: Fitur cuaca (luas panen, curah hujan, kelembapan, suhu rata-rata).
- **Output**: Prediksi produksi padi (ton).

### Arsitektur Model:
1. **Dense Layer** - 128 neuron (ReLU)
2. **Dropout** - 20%
3. **Dense Layer** - 64 neuron (ReLU)
4. **Dropout** - 20%
5. **Dense Layer** - 32 neuron (ReLU)
6. **Dense Layer** - 16 neuron (ReLU)
7. **Dense Layer** - 1 neuron (Linear Activation)

---

## 📊 Dataset
Data berasal dari sumber berikut :
'https://www.kaggle.com/datasets/ardikasatria/datasettanamanpadisumatera'
Dataset yang digunakan diambil mencakup informasi berikut:
- **Luas Panen** (hektar)
- **Curah Hujan** (mm)
- **Kelembapan** (%)
- **Suhu Rata-rata** (°C)
- **Produksi** (ton)

---

## 👤 Dikembangkan oleh
[Nama Anda]
