import io
import os

from rich import print
from googleapiclient.http import MediaIoBaseDownload


def bajar_datos(nombre, drive):
    """Usando la API de Google Drive bajar un archivo que contenga datos

    Parámetros
    ----------
    nombre:     string
                Nombre del archivo que se quiere obtener de Google Drive

    extension:  string
                Extensión que corresponde al nombre del archivo que se quiere obtener
                Los valores aceptados son 'xlsx' o 'csv'

    Salida
    ------

    """

    mimetypes_spreadsheets = ['text/csv',
                              'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                              'application/x-vnd.oasis.opendocument.spreadsheet',
                              'application/wps-office.xlsx']

    mimetaip, archivo_id = buscar_archivo(nombre, drive)

    if mimetaip == 'application/vnd.google-apps.spreadsheet':
        mimetype_exportar = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        request = drive.files().export_media(fileId=archivo_id,
                                             mimeType=mimetype_exportar)
        path_archivo = os.path.join('servicios', 'datos', nombre + '.xlsx')

        with open(path_archivo, 'wb') as archivo:
            archivo.write(bajar_archivo(request))
        print('[green3]   :arrow_right: Se obtuvo el archivo[/green3] ' +
              '[green3 italic]' + nombre + '.xlsx' + '[/green3 italic]')

    elif mimetaip in mimetypes_spreadsheets:
        request = drive.files().get_media(fileId=archivo_id)
        path_archivo = os.path.join('servicios', 'datos', nombre)

        with open(path_archivo, 'wb') as archivo:
            archivo.write(bajar_archivo(request))
        print('[green3]   :arrow_right: Se obtuvo el archivo[/green3] '
              + '[green3 italic]' + nombre + '[/green3 italic]')

    else:
        print("[red1]   :no_entry:  Este tipo de archivo no es válido D:[/red1]")
        print("[red1]      Intenta de nuevo con un xlsx o un csv[/red1]")
        print("")
        print("[magenta3 bold]Baaaiiii, ¡vuelva pronto! :D[/magenta3 bold]")


def buscar_archivo(nombre, drive):

    try:
        variable_nombre = 'name=' + '"' + nombre + '"'
        archivo = drive.files().list(q=variable_nombre,
                                     fields='files(id, name, mimeType)',
                                     pageToken=None).execute().get('files', [])
        mimetaip = archivo[0]['mimeType']
        archivo_id = archivo[0]['id']

    except IndexError as error:
        print("[red1]   :no_entry:  Ese archivo no existe D:[/red1]")
        print("[red1]      Verifica el nombre[/red1]")
        print("")
        print("[magenta3 bold]Baaaiiii, ¡vuelva pronto! :D[/magenta3 bold]")
        mimetaip = None
        archivo_id = None
        exit()

    return mimetaip, archivo_id


def bajar_archivo(request):

    archivo_bits = io.BytesIO()
    downloader = MediaIoBaseDownload(archivo_bits, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    archivo_obtenido = archivo_bits.getvalue()

    return archivo_obtenido
