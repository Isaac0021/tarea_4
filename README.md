# Heart Disease Prediction 

Este proyecto implementa un modelo de Machine Learning que predice el riesgo de enfermedad cardíaca en una persona, 
con base en variables clínicas y de estilo de vida. Cuenta con una interfaz gráfica construida con Streamlit, 
un sistema de reentrenamiento automático usando GitHub Actions, y versionamiento de datos con DVC en almacenamiento en la nube (Azure Blob Storage).

## ¿Cómo ejecutar la aplicación?

### 1. Clonar el repositorio

```bash
git clone https://github.com/Isaac0021/tarea_4.git
cd tarea_4
```

### 2. Instalar dependencias 

python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
pip install -r requirements.txt

### 3. Ejecutar app streamlit 

streamlit run app/app.py

### 4. Descripción modelo 

Campo | Descripción | Tipo

Edad | Edad del paciente (18–100 años) | Entero

Género | Mujer / Hombre | Categórico

Estatura | Estatura en centímetros | Entero

Peso | Peso en kilogramos | Entero

Presión Sistólica | Presión arterial máxima (mm Hg) | Entero

Presión Diastólica | Presión arterial mínima (mm Hg) | Entero

Colesterol | Normal / Alto / Muy alto | Categórico

Glucosa | Normal / Alta / Muy alta | Categórico

¿Fuma? | Sí / No | Binario

¿Toma alcohol? | Sí / No | Binario

¿Es físicamente activo? | Sí / No | Binario

¿Fuma?	Sí / No	Binario

¿Toma alcohol?	Sí / No	Binario

¿Es físicamente activo?	Sí / No	Binario

### Salida del modelo 

La salida del modelo es un número:

- `0`: Sin riesgo aparente de enfermedad cardiovascular
- `1`: Riesgo presente de enfermedad cardiovascular
