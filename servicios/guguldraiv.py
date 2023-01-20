import io
import os
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

    print("hasta aqui si jala")
    print(mimetaip)
    print(id)

    if mimetaip == 'application/vnd.google-apps.spreadsheet':
        request = drive.files().export_media(fileId=id, mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        path_archivo = os.path.join('servicios', 'datos', nombre + '.xlsx')

        with open(path_archivo, 'wb') as archivo:
            archivo.write(bajar_archivo(request))
        print("google spreadsheets abajo")

    elif mimetaip == 'text/plain' or mimetaip == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        request = drive.files().get_media(fileID=id, mimeType = mimetaip)
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
        # archivo = io.BytesIO()
        # downloader = MediaIoBaseDownload(archivo, request)
        # done = False
        # while done is False:
        #     status, done = downloader.next_chunk()
        #     print(F'Download {int(status.progress() * 100)}.')
        # request = drive.files().export_media(fileId=id,
        #                                      mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        #
        # file = io.BytesIO()
        # downloader = MediaIoBaseDownload(file, request)
        # done = False
        # while done is False:
        #     status, done = downloader.next_chunk()
        #     print(F'Download {int(status.progress() * 100)}.')
        # print(file.getvalue())

        #Hay que moverse al repo donde se desea bajar el contenido del archivo
        # elif mimetaip == 'texto/plain' or mimetaip == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        #     if 'csv' in nombre:
        #         print("aun no")
        #     else:
        #         print("[]Este tipo de archivo no es válido D:[]")
        #         print("[]Intenta de nuevo con un xlsx o un csv[]")
        #         print("[]Baaaiiii, ¡vuelva pronto! :D[]")
        # else:
        #     print("[]Este tipo de archivo no es válido D:[]")
        #     print("[]Intenta de nuevo con un xlsx o un csv[]")
        #     print("[]Baaaiiii, ¡vuelva pronto! :D[]")

def buscar_archivo(nombre, drive):

    archivo = drive.files().list(q='name=' + nombre,
                               fields='files(id, name, mimeType)',
                               pageToken=None).execute().get('files', [])
    mimetaip = archivo[0]['mimeType']
    id = archivo[0]['id']

    return mimetaip, id


def bajar_archivo(request):

    archivo_bits = io.BytesIO()
    downloader = MediaIoBaseDownload(archivo_bits, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(F'Download {int(status.progress() * 100)}.')

    archivo_obtenido = archivo_bits.getvalue()

    return archivo_obtenido



