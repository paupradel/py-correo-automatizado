import io
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

    mimetaip, id = buscar_archivo(nombre, drive)

    if mimetaip == 'application/vnd.google-apps.spreadsheet':
        request = drive.files().get_media(fileId=id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')
        print(file.getvalue())
    elif mimetaip == 'texto/plain' or mimetaip == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        if 'csv' in nombre:
            print("aun no")
        else:
            print("[]Este tipo de archivo no es válido D:[]")
            print("[]Intenta de nuevo con un xlsx o un csv[]")
            print("[]Baaaiiii, ¡vuelva pronto! :D[]")
    else:
        print("[]Este tipo de archivo no es válido D:[]")
        print("[]Intenta de nuevo con un xlsx o un csv[]")
        print("[]Baaaiiii, ¡vuelva pronto! :D[]")


def buscar_archivo(nombre, drive):

    archivo=drive.files().list(q="name='intercambio_dai_2022'",
                               fields='files(id, name, mimeType)',
                               pageToken=None).execute().get('files', [])
    mimetaip = archivo[0]['mimeType']
    id = archivo[0]['id']

    return mimetaip, id



