import pandas as pd

import os
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client import file
from email.message import EmailMessage
from rich import print

from servicios.guguldraiv import bajar_datos

print("[bold cyan1]¿Listx para enviar correos automatizados?[/bold cyan1]")
print("[bold cyan1]¡Pues vamos![/bold cyan1]")

time.sleep(2.5)

# Autenticación y apertura de sesión en Google Drive y Gmail
store = file.Storage(os.path.join('credenciales', 'storage.json'))
credenciales = store.get()

# Se llaman a las API's
gmail = build('gmail', 'v1', credentials=credenciales)
drive = build('drive', 'v3', credentials=credenciales)

print("")
print("[green3]Autenticación en Google finalizada[/green3]")

# archivos = drive.files().list(pageSize=10).execute().get('files', [])
# for archivo in archivos:
#     print(archivo['name'])

# Obtención del archivo de google drive

print("[green3]Obteniendo archivo con datos[/green3]")

# nombre = 'intercambio_dai_2022'
# nombre = '210802ReporteTendenciaSemanal.pdf'
# nombre = 'limipio_tiraderos_clandestinos.csv'
# nombre = 'diccionario_tiraderos_cdmx.xlsx'
nombre = 'EsferaGigante.xlsx'
# nombre = 'Esferagiganteeeee.xlsx'


bajar_datos(nombre, drive)

# datos = 'intercambio_dai_2022.xlsx'


# Asignación de variables para construir el correo


# Construcción del correo


# Envio de correos

