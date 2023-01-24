import base64
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from googleapiclient.errors import HttpError



def enviar_mensaje(gmail):
    """Enviar un mensaje de gmail"""

    try:
        cuerpo_msj = """
        <html>
          <body>
            <p> Esto es un <b>párrafo</b> de prueba </p>
          </body>
        </html>"""

        mensaje_html = MIMEText(cuerpo_msj, 'html')
        mensaje_html['To'] = 'pamppsteaching@gmail.com'
        mensaje_html['From'] = 'pradel.paulina@gmail.com'
        mensaje_html['Subject'] = 'Probando probando'

        mensaje_cifrado = base64.urlsafe_b64encode(mensaje_html.as_bytes()).decode()

        crear_mensaje = {
            'raw': mensaje_cifrado
        }

        enviando_mensaje = (gmail.users().messages().send(userId='me',
                                                          body=crear_mensaje).execute())
        print(F'Message Id: {enviando_mensaje["id"]}')

    except HttpError as error:
        print(F'Ocurrió un error: {error}')
        enviando_mensaje = None

    return enviando_mensaje


# def enviar_mensaje(gmail):
#     """Enviar un mensaje de gmail"""
#
#     try:
#         mensaje = EmailMessage()
#         mensaje.set_content('Este es un correo automatizado')
#
#         mensaje['To'] = 'pamppsteaching@gmail.com'
#         mensaje['From'] = 'pradel.paulina@gmail.com'
#         mensaje['Subject'] = 'Probando probando'
#
#         mensaje_cifrado = base64.urlsafe_b64encode(mensaje.as_bytes()).decode()
#
#         crear_mensaje = {
#             'raw': mensaje_cifrado
#         }
#
#         enviando_mensaje = (gmail.users().messages().send(userId='me',
#                                                           body=crear_mensaje).execute())
#         print(F'Message Id: {enviando_mensaje["id"]}')
#
#     except HttpError as error:
#         print(F'Ocurrió un error: {error}')
#         enviando_mensaje = None
#
#     return enviando_mensaje


