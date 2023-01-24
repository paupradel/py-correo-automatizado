import base64

from rich import print
from email.mime.text import MIMEText
from googleapiclient.errors import HttpError


def enviar_mensaje(gmail, email_destinatario, variable_uno, variable_dos):
    """Enviar un mensaje de gmail

    Parámetros
    ----------
    gmail:     función
               Llamar al servicio de Gmail para usar su API, eso se hace en aplicacion.py

    email_destinatario:  string
                         dirección de correo electrónico de la persona destinataria

    variable_uno: string
                  texto a insertar en el cuerpo del correo y que varía dependiendo de email_destinatario

    variable_dos: string
                  texto a insertar en el cuerpo del correo y que varía dependiendo de email_destinatario

    Salida
    ------

    enviando_mensaje: Se envía el correo electrónico de acuerdo a los parámetros o se envía un mensaje de error
                      en caso contrario
    """

    try:
        cuerpo_msj = F"""
        <html>
          <body>
            <p> Hola <b>{variable_uno}</b>,</p>
            <p> El artículo de interés es {variable_dos}.</p> 
            <p> Esto es un <b>correo de prueba.</p>
            <br>
            <p> Que tengas buen día :D</p>
          </body>
        </html>"""

        mensaje_html = MIMEText(cuerpo_msj, 'html')
        mensaje_html['To'] = email_destinatario
        mensaje_html['Subject'] = 'Correo de prueba'

        mensaje_cifrado = base64.urlsafe_b64encode(mensaje_html.as_bytes()).decode()

        crear_mensaje = {
            'raw': mensaje_cifrado
        }

        enviando_mensaje = (gmail.users().messages().send(userId='me',
                                                          body=crear_mensaje).execute())
        print(F'[magenta3 ]Mensaje enviado a: {variable_uno}[/magenta3]')

    except HttpError as error:
        print(F'Ocurrió un error: {error}')
        enviando_mensaje = None

    return enviando_mensaje
