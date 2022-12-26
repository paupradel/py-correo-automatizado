# py-correo-automatizado

Este proyecto es una aplicación simple para obtener un archivo remoto por medio de la API de Google Drive, para 
después importarlo y leerlo como un dataframe de pandas. Los datos de dicho dataframe armarán n cantidad de 
borradores de correo electrónico y se enviarán usando la API de Gmail.

# Requerimientos

Por medio del archivo `Pipfile` o el `requirements.txt` es posible instalar las dependencias de este proyecto. Para 
usar el `Pipfile` es necesario tener instalado [Pipenv](https://pipenv.pypa.io/en/latest/) y crear un ambiente 
virtual como se indique en la documentación. El archivo `requirments.txt` se puede utilizar con cualquier otra 
herramienta para crear ambientes virtuales de Python. De cualquier manera es muy recomendable crear un ambiente 
virtual para el uso de este proyecto y evitar la instalación de los requerimientos de manera global. 

En este proyecto se usa `Python 3.10` y sus dependencias principales se listan a continuación:

- [Pandas](https://pandas.pydata.org/)
- [Biblioteca cliente de la API de Google](https://github.com/googleapis/google-api-python-client)

Para familiarizarse con el uso de las API's de Google usando Python, se puede realizar este 
[ejercicio de codelab en google](http://g.co/codelabs/gsuite-apis-intro).

# Uso

1. [Clona](https://git-scm.com/docs/git-clone) este repositorio en tu computadora e instala las dependencias.
2. Instala las dependencias según lo recomentado en la sección anterior.


# API's de Google

Trabajar con las API's de Google con Python no es tan directo como uno pensaría. Existen 
[ciertos wrappers](https://github.com/googlearchive/PyDrive) de algunas de ellas que hacen el trabajo más sencillo y 
que funcionan bastante bien, pero siempre es bonito ensuciarnos un poco las manos para aprender mucho más. Si te 
interesa agregar funcionalidades a este código para adaptarlo a tus necesidades, tendrás que ensuciarte las manos con 
las API's de Google. Para hacer tu vida más sencilla pondré acá algunos enlaces útiles que me sirvieron bastante 
para poder construir esta aplicación.

Dentro de la documentación de la API de Google Drive se encuentra este 
[ejercicio de codelab](http://g.co/codelabs/gsuite-apis-intro) con Python que te enseñará entre otras cosas a obtener 
las credenciales para tu aplicación, crear un proyect en la consola de desarrolladorxs de Google, aprender acerca de 
las [bibliotecas cliente de la API de Google](https://developers.google.com/api-client-library/), etc.


# Contacto

- Paulina Pradel (pradel.paulina@gmail.com)
