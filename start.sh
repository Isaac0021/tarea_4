#!/bin/bash

echo "Configurando DVC remoto..."
dvc remote modify azure-remote connection_string "$DVC_AZURE_CONN"

echo "Descargando archivos versionados con DVC..."
dvc pull

echo "Iniciando Streamlit..."
streamlit run app/app.py