import streamlit as st
import joblib
import pandas as pd
import os

path_modelo = os.path.join(os.path.dirname(__file__), "modelo.pkl")
modelo = joblib.load(path_modelo)

st.title("Heart Disease Prediction")
st.markdown("""Ingrese los datos del paciente para evaluar el riesgo de enfermedad cardiovascular.""")

age = st.slider("Edad (años)", 20, 80, 50)
gender = st.radio("Género", ["Mujer", "Hombre"])
height = st.number_input("Estatura (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Peso (kg)", min_value=30, max_value=200, value=70)
ap_hi = st.number_input("Presión Sistólica", value=120)
ap_lo = st.number_input("Presión Diastólica", value=80)
chol = st.selectbox("Colesterol", ["Normal", "Alto"])
gluc = st.selectbox("Glucosa", ["Normal", "Alto"])
smoke = st.selectbox("¿Fuma?", ["No", "Sí"])
alco = st.selectbox("¿Toma alcohol?", ["No", "Sí"])
active = st.selectbox("¿Es activo físicamente?", ["No", "Sí"])

input_dict = {
    "age": age,
    "gender": 0 if gender == "Mujer" else 1,
    "height": height,
    "weight": weight,
    "ap_hi": ap_hi,
    "ap_lo": ap_lo,
    "cholesterol": 0 if chol == "Normal" else 1,
    "gluc": 0 if gluc == "Normal" else 1,
    "smoke": 0 if smoke == "No" else 1,
    "alco": 0 if alco == "No" else 1,
    "active": 0 if active == "No" else 1
}

input_df = pd.DataFrame([input_dict])

if st.button("Predecir"):
    prediction = modelo.predict(input_df)[0]
    st.success("Resultado: {}".format("🛑 Riesgo de enfermedad cardiovascular" if prediction == 1 else "✅ No se detecta riesgo significativo"))