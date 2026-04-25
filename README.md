# AI DRIVEN INTRUSION DETECTION SYSTEMS USING DEEP LEARNING

1) Overview:
This project is an AI-based Intrusion Detection System that uses an LSTM (Long Short-Term Memory)
neural network to detect malicious network traffic.

## Research Background
This project was developed as part of a research study focused on improving intrusion detection systems using deep learning techniques. Traditional IDS models often suffer from high false positive rates and struggle to detect modern attack patterns. 

To address this, an LSTM-based deep learning model was designed to analyze sequential network traffic data and identify anomalies more effectively. The model was trained and evaluated on the NSL-KDD dataset using metrics such as accuracy, precision, recall, and F1-score.

The results demonstrated improved detection performance and reduced false positives compared to traditional machine learning approaches.

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

