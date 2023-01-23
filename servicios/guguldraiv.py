import io
import os
from rich import print
from googleapiclient.http import MediaIoBaseDownload


def descargar_archivo(nombre, drive):
    """Usando la API de Google Drive bajar un archivo que contenga datos

    Parámetros
    ----------
    nombre:     string
                Nombre del archivo que se quiere obtener de Google Drive

    drive:      función
                Llamar al servicio de Google Drive para usar su API, esto se hace en aplicacion.py

    Salida
    ------
    Se descarga el archivo indicado por la variable nombre en la carpeta /datos

    """

    # Lista que contiene los MIME TYpe más comunes para convertirse a dataframes de pandas
    mimetypes_spreadsheets = ['text/csv',
                              'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                              'application/x-vnd.oasis.opendocument.spreadsheet',
                              'application/wps-office.xlsx']

    mimetaip, archivo_id = buscar_archivo(nombre, drive)

    if mimetaip == 'application/vnd.google-apps.spreadsheet':
        mimetype_exportar = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        request = drive.files().export_media(fileId=archivo_id,
                                             mimeType=mimetype_exportar)
        path_archivo = os.path.join('datos', nombre + '.xlsx')

        with open(path_archivo, 'wb') as archivo:
            archivo.write(descargar_datos(request))
        print('[green3]   :arrow_right: Se obtuvo el archivo[/green3] ' +
              '[green3 italic]' + nombre + '.xlsx' + '[/green3 italic]')

    elif mimetaip in mimetypes_spreadsheets:
        request = drive.files().get_media(fileId=archivo_id)
        path_archivo = os.path.join('datos', nombre)

        with open(path_archivo, 'wb') as archivo:
            archivo.write(descargar_datos(request))
        print('[green3]   :arrow_right: Se obtuvo el archivo[/green3] '
              + '[green3 italic]' + nombre + '[/green3 italic]')

    else:
        print("[red1]   :no_entry:  Este tipo de archivo no es válido D:[/red1]")
        print("[red1]      Intenta de nuevo con un xlsx o un csv[/red1]")
        print("")
        print("[magenta3 bold]Baaaiiii, ¡vuelva pronto! :D[/magenta3 bold]")


def buscar_archivo(nombre, drive):
    """Buscar un archivo en Google Drive dado su nombre

    Parámetros
    ----------
    nombre:     string
                Nombre del archivo que se quiere buscar en Google Drive

    drive:      función
                Llamar al servicio de Google Drive para usar su API, esto se hace en aplicacion.py

    Salida
    ------
    mimetaip:   string
                MIME Type obtenido de los metadatos del archivo buscado y encontrado en Google Drive
                
    archivo_id: string
                Id de Google Drive del archivo buscado y encontrado
    """

    try:
        variable_nombre = 'name=' + '"' + nombre + '"'
        archivo = drive.files().list(q=variable_nombre,
                                     fields='files(id, name, mimeType)',
                                     pageToken=None).execute().get('files', [])
        mimetaip = archivo[0]['mimeType']
        archivo_id = archivo[0]['id']

    except IndexError:
        print("[red1]   :no_entry:  Ese archivo no existe D:[/red1]")
        print("[red1]      Verifica el nombre[/red1]")
        print("")
        print("[magenta3 bold]Baaaiiii, ¡vuelva pronto! :D[/magenta3 bold]")
        mimetaip = None
        archivo_id = None
        exit()

    return mimetaip, archivo_id


def descargar_datos(request):
    """Obtener datos del archivo buscado para después ser exportado o descargado directamente dependiendo
    de su MIME Type en la función 'descargar_archivo'
    
    Parámetros
    ----------
    request:    response object
                Datos en respuesta a la petición hecha a la API de Google Drive. Se indica el MIME Type con el que
                se exporta o descarga el archivo dependiendo de si pertenece al Google Workspace o no
    
    Salida
    ------
    archivo_obtenido: bytes (datos binarios)
                      Se obtiene el archivo en formato binario para ser exportado o descargado posteriormente de
                      acuerdo a su MIME Type
    """
    archivo_bits = io.BytesIO()
    downloader = MediaIoBaseDownload(archivo_bits, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    archivo_obtenido = archivo_bits.getvalue()

    return archivo_obtenido
