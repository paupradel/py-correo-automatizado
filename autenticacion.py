import os

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

archivo_credenciales = 'credenciales.json'

scopes = 'https://www.googleapis.com/auth/drive.readonly.metadata https://www.googleapis.com/auth/drive.readonly https://www.googleapis.com/auth/gmail.compose'
store = file.Storage(os.path.join('credenciales', 'storage.json'))
credenciales = store.get()

if not credenciales or credenciales.invalid:
    flow = client.flow_from_clientsecrets(os.path.join('credenciales', archivo_credenciales), scopes)
    credenciales = tools.run_flow(flow, store)

drive = discovery.build('drive', 'v3', http=credenciales.authorize(Http()))


# Probar el funcionamiento de la API de Google Drive
archivos = drive.files().list(pageSize=10).execute().get('files', [])
for archivo in archivos:
    print(archivo['name'])
