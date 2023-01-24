import os
import time

from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
from oauth2client import file
# from email.message import EmailMessage
from rich import print

from servicios.guguldraiv import descargar_archivo
from servicios.yimeil import enviar_mensaje
from auxiliar.estructurar_correo import leer

print("[bold cyan1]¿Listx para enviar correos automatizados?[/bold cyan1]")
print("[bold cyan1]¡Pues vamos![/bold cyan1]")

time.sleep(2.5)

# Autenticación y apertura de sesión en Google Drive y Gmail
store = file.Storage(os.path.join('credenciales', 'storage.json'))
credenciales = store.get()

# Se llaman a las API
gmail = build('gmail', 'v1', credentials=credenciales)
drive = build('drive', 'v3', credentials=credenciales)

print("")
print("[green3]Autenticación en Google finalizada[/green3]")

# archivos = drive.files().list(pageSize=10).execute().get('files', [])
# for archivo in archivos:
#     print(archivo['name'])

# Obtención del archivo de google drive

print("[green3]Obteniendo archivo con datos[/green3]")

# nombre = ''
nombre = 'intercambio_dai_2022'
# nombre = '210802ReporteTendenciaSemanal.pdf'
# nombre = 'limipio_tiraderos_clandestinos.csv'
# nombre = 'diccionario_tiraderos_cdmx.xlsx'
# nombre = 'EsferaGigante.xlsx'
# nombre = 'Esferagiganteeeee.xlsx'

if nombre == '':
    print("[red1]   :no_entry:  No has cambiado la variable [italic]nombre[/italic] D:[/red1]")
    print("")
    print("[magenta3 bold]Baaaiiii, ¡vuelva pronto! :D[/magenta3 bold]")
    exit()


archivo_descargado = descargar_archivo(nombre, drive)

print("[green3]Leyendo el archivo descargado[/green3]")

# datos = 'intercambio_dai_2022.xlsx'

datos = leer(archivo_descargado, 'datos_dummy')

print(datos.head())

# Asignación de variables para construir el correo

# correo_destinataria = 'email_destinatario'
# asunto = 'Probando esta aplicación'
# composicion_correo = ['variable_uno', 'variable_dos', 'variable_tres']

# correo_destinataria = 'email_destinatario'
# asunto = 'Intercambio amistDAI 2023'
# composicion_correo = ['nombre_destinatario', 'persona_recibe',
#                       'opcion_uno', 'liga_opcion_uno',
#                       'opcion_dos', 'liga_opcion_dos',
#                       'opcion_tres', 'liga_opcion_tres',
#                       'nombre_persona_recibe',
#                       'calle_y_numero',
#                       'colonia',
#                       'municipio_alcaldia',
#                       'codigo_postal',
#                       'ciudad',
#                       'estado',
#                       'pais',
#                       'referencias']

enviar_mensaje(gmail)
