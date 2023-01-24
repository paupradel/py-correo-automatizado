import pandas as pd


def leer(archivo_descargado, sheet=None):
    """Obtener un dataframe de pandas dependiendo del tipo de archivo

    Parámetros
    ----------
    archivo_descargado:  string
                         Nombre del archivo descargado de Google Drive

    sheet:      string
                Nombre de la hoja en caso de que sea un archivo xlsx, por default es None

    Salida
    ------
    dataframe: dataframe de pandas
               Conjunto de datos que sirven para componer los correos a enviar
    """

    dataframe = pd.DataFrame()
    if 'xlsx' in archivo_descargado:
        dataframe = pd.read_excel(archivo_descargado, sheet_name=sheet)
    elif 'csv' in archivo_descargado:
        dataframe = pd.read_csv(archivo_descargado)

    return dataframe
