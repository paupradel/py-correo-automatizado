import os

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# Rutas generales

donde_credenciales = os.path.join('credenciales')
archivo_credenciales = 'credenciales.json'

SCOPES = ('https://www.googleapis.com/auth/drive.readonly.metadata',
          'https://www.googleapis.com/auth/gmail')
store = file.Storage(os.path.join(donde_credenciales, 'storage.json'))
credenciales = store.get()

if not credenciales or credenciales.invalid:
    flow = client.flow_from_clientsecrets(os.path.join(donde_credenciales, archivo_credenciales, SCOPES))
    credenciales = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=credenciales.authorize(Http()))

# Probar el funcionamiento de la API de Google Drive

files = DRIVE.files().list().execute().get('files', [])
for f in files:
    print(f['name'], f['mimeType'])