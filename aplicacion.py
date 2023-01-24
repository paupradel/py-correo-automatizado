import os
import time

from googleapiclient.discovery import build
from oauth2client import file
from rich import print

from servicios.guguldraiv import descargar_archivo
from servicios.yimeil import enviar_mensaje
from auxiliar.leer import leer

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

# Variables a establecer
nombre = ''  # Archivo alojado en Google Drive de donde obtendrás los datos para componer el correo
hoja = ''  # El nombre de la hoja en caso de que sea un archivo xlsx o existan múltiples hojas en el mismo
correo_destinatario = 'email_destinatario'  # Nombre de la columna que trae los correos de las personas destinatarias
composicion_correo = ['variable_uno', 'variable_dos']  # Nombres de las columnas para componer el correo

if nombre == '':
    print("[red1]:no_entry:  No has cambiado la variable [italic]nombre[/italic] D:[/red1]")
    print("")
    print("[magenta3 bold]Continuaré con el archivo de datos dummy para enviar correos de prueba :D[/magenta3 bold]")
    print("[magenta3 bold]Recuerda poner el nombre del archivo a descargar para enviar tus correos[/magenta3 bold]")
    datos = leer(os.path.join('datos', 'dummy.csv'))
else:
    print("[green3]Obteniendo archivo con datos[/green3]")
    archivo = descargar_archivo(nombre, drive)
    print("[green3]Leyendo el archivo descargado[/green3]")
    datos = leer(archivo, hoja)


print("[green3]Enviando correos automatizados[/green3]")
for indice, fila in datos.iterrows():
    enviar_mensaje(gmail,
                   fila[correo_destinatario],
                   fila[composicion_correo[0]],
                   fila[composicion_correo[1]])

print("")
print("[bold cyan1]Gracias por usar esta aplicación, vuelve pronto :heart: [/bold cyan1]")
