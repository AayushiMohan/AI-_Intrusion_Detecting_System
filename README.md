# Intrusion Detection System using LSTM

1) Overview
This project is an AI-based Intrusion Detection Systemthat uses an LSTM (Long Short-Term Memory)
neural network to detect malicious network traffic.

2) Features
- Detects normal vs attack traffic
- Uses deep learning (LSTM)
- Trained on NSL-KDD dataset
- Visualizes accuracy and loss

3) Technologies Used
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Streamlit

4) Project Structure
- AI_Intrusion_Detection_System.ipynb → Model training
- app.py → Streamlit web app
- ids_model.keras → Saved model
- IDS_requirements.pdf → Installation guide

5) How to Run

Install dependencies:
pip install tensorflow numpy pandas matplotlib streamlit

6) Run the app:
streamlit run app.py

7) Output
The model predicts whether the input network traffic is normal or an attack.

