import os

import pandas as pd

from rich import print


def leer(archivo_descargado, hoja=None):

    datos = pd.DataFrame()

    if 'xlsx' in archivo_descargado:
        datos = pd.read_excel(archivo_descargado, sheet_name=hoja)
    elif 'csv' in archivo_descargado:
        datos = pd.read_csv(archivo_descargado)

    return datos


# 'Hola' + variable_uno + '. El artículo de interés es ' + variable_dos + ', y lo podrás encontrar en este enlace ' +
# variable_tres +
# 'Espero que esta prueba haya funcionado.'


