import pandas as pd

import os

import google.auth

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client import file
from email.message import EmailMessage


# Autenticación y apertura de sesión en Google Drive y Gmail

store = file.Storage(os.path.join('credenciales', 'storage.json'))
credenciales = store.get()

gmail = build('gmail', 'v1', credentials=credenciales)
drive = build('drive', 'v3', credentials=credenciales)

archivos = drive.files().list(pageSize=10).execute().get('files', [])
for archivo in archivos:
    print(archivo['name'])


# Obtención del archivo de google drive

# datos = 'intercambio_dai_2022.xlsx'


# Asignación de variables para construir el correo


# Construcción del correo


# Envio de correos

