FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todo el contenido al contenedor
COPY . .

# Instalar requirements
RUN pip install --no-cache-dir -r requirements.txt

# Puerto que usará Streamlit
EXPOSE 8501

# Comando para ejecutar Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.enableCORS=false"]
