# py-correo-automatizado

Aplicación simple para obtener un archivo remoto por medio de la API de Google Drive, para 
después importarlo y leerlo como un dataframe de pandas. Los datos de dicho dataframe armarán _N_ cantidad de 
borradores de correo electrónico y se enviarán usando la API de Gmail.

## Acerca de este proyecto

Como buena persona programadora, a veces me gusta complicarme la vida y pasar muchas horas automatizando una tarea que 
probablemente me tome dos horas hacerla de un jalón :3. Y pues bien, en el lugar donde trabajo tuvimos la iniciativa de 
realizar un intercambio virtual navideño. Soy la encargada de crear un formulario para que las personas registren sus 
preferencias de regalo y sus datos de contacto. Después también debo de enviar _N_ cantidad de mails para informar a 
cada persona los resultados del sorteo, direcciones, etc. Así que aprovechando que los resultados del formulario de 
google arrojan un spreadsheets de datos, se me ocurrió contruir esta aplicación aprovechando las bondades (o no) de las 
API's de google.

No sé si exista una manera más fácil de hacer esto y evitar la programación, pero de cualquier manera **este es un 
excelente ejercicio para mi, y para seguir practicando mi python**.

Gracias si llegaste hasta aquí y espero que esta aplicación te sirva.

### Las API's de Google

Trabajar con las API's de Google con Python no es tan directo como uno pensaría. Existen
[ciertos wrappers](https://github.com/googlearchive/PyDrive) de algunas de ellas que hacen el trabajo más sencillo y
que funcionan bastante bien, pero siempre es bonito ensuciarnos un poco las manos para aprender mucho más. Si te
interesa agregar funcionalidades a este código para adaptarlo a tus necesidades, tendrás que ensuciarte las manos. 
Para hacer tu vida más sencilla pondré acá algunos enlaces útiles que me sirvieron bastante
para poder construir esta aplicación y puedas pasar a la sección de _Instalación e Instrucciones_ mejor informadx.

Dentro de la documentación de la API de Google Drive se encuentra este
[ejercicio de codelab](http://g.co/codelabs/gsuite-apis-intro) con Python que te enseñará entre otras cosas a obtener
las credenciales para tu aplicación, crear un proyecto en la consola de desarrolladorxs de Google, aprender acerca de
las [bibliotecas cliente de la API de Google](https://developers.google.com/api-client-library/), entre otra cosas.

#### Los `scopes`

Dependiendo de lo que necesites trabajar u obtener de las diferentes API's de Google es a como vas a configurar unas 
variables llamas `scopes`. En este proyecto existe un archivo llamado `autenticacion.py` que tendrás que ejecutar la 
primera vez que uses este código para que le des permiso a tu cuenta de google de acceder a este proyecto (aplicación 
web). En este archivo modificarás los `scopes`, que para este proyecto lucen así:

```python
scopes = 'https://www.googleapis.com/auth/drive.readonly.metadata https://www.googleapis.com/auth/gmail.compose'
```

En el primer scope, estamos pidiendo permiso para ver los metadatos de los archivos que se encuentran en Google Drive, y 
en el segundo scope se esta pidiendo permiso para crear, leer, actualizar y eliminar borradores, así como enviar 
mensajes y borradores.

Los `scopes` completos de la API de Google Drive los puedes encontrar 
[aquí](https://developers.google.com/drive/api/guides/api-specific-auth) y los de la API de Gmail
[acá](https://developers.google.com/gmail/api/auth/scopes).

Puedes agregar la cantidad de `scopes` que necesites a la variable, sin embargo es necesario tener cuidado pues estás 
dando potencial acceso de datos sensibles a una aplicacióne externa. Te recomiendo que verifiques muy bien en la 
documentación el tipo de uso (Recomendado, Sensible y Restringido) que tiene cada `SCOPE`.

Cabe mencionar que los `scopes` usados aquí están marcados con `Restringido`, por lo que la primera vez que se
abra la ventana en tu navegador para dar permiso a la aplicación te aparecerá un advertencia de que esta aún no está
verificada. Esto es porque Google requiere que se lleve a cabo un proceso de verificación cuando las aplicaciones web
accesan a ciertos datos sensibles para el usuario. Dado que tu como persona usuaria estas construyendo tu propia 
aplicación web en la consola de Google y a este código le estás dando acceso a tu cuenta de Google, no debería de 
haber ningún problema. Bajo ninguna circunstancia al correr esta aplicación yo como autora del código tendré acceso a 
tus datos. Es posible que en un futuro someta esta aplicación web a verificación, simplemente por trámite administrativo 
y para que ya no aparezca la ventana de advertencia. Para aprender más acerca de la verificación de las aplicaciones 
web externas, puedes ir a [este enlace](https://support.google.com/cloud/answer/10311615#verification-status).


## Requerimientos

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

## Instalación e instrucciones

### Inicio
1. [Clona](https://git-scm.com/docs/git-clone) este repositorio en tu computadora e instala las dependencias.
2. Instala las dependencias según lo recomendado en la sección anterior.

### Configurar la API de Google drive por primera vez

Lo descrito en esta sección sólo es necesario ejectuarlo una sola vez para dar permisos a la aplicación.

3. [Crea un proyecto](https://developers.google.com/workspace/guides/create-project) en la consola de 
desarrolladorxs de Google y dale un nombre.
4. [Habilita las API's](https://developers.google.com/workspace/guides/enable-apis) de Google necesarias. En este 
proyecto se necesitan las API's de Google Drive y de Gmail.
5. [Autoriza el uso de tu aplicación, crea las credenciales](https://console.cloud.google.com/apis/credentials) 
para tu proyecto.
6. Baja de la consola de tu proyecto el archivo `.JSON` que contiene las credenciales y colócalo en la carpeta
`/credenciales`. Le puedes dar el nombre que tu quieras, pero por default aquí este archivo 
se llama `credenciales.json`. Si deseas cambiarle el nombre, puedes ir a `autenticacion.py` y modificar la variable 
`archivo_credenciales`.
7. Crea en la carpeta `/credenciales` un archivo de nombre `storage.json`. En este archivo se guardará el token de
acceso una vez que autorices el uso de la aplicación web. Este archivo junto con el `credenciales.json` y toda 
la carpeta `/credenciales` están marcados en el `.gitignore` para no ser subidos al repositorio de github. Cada vez 
que agregues o modifiques los `scopes` en el archivo `autenticacion.py` es necesario que borres el archivo 
`storage.json` y vuelvas a correr la autenticación.
8. Corre el archivo `autenticacion.py`, haciendo `python autenticacion.py`. Se abrirá una ventana en tu navegador que 
mostrará una advertencia (ir a la sección de `scopes` más arriba para conocer más) o bien te pedirá que des permiso 
con tu cuenta de Google a los `scopes` utilizados.
9. Si todo salió correctamente en la misma ventana de tu navegador aparecerá un mensaje que indicará que la 
autenticación fue exitosa. También en tu consola aparecerá una lista de los primeros 10 archivos que se encuentran en 
tu Google Drive (creados, abiertos, o compartidos por y hacia ti).


### Ejecutar la aplicación para mandar _N_ mails
10. 





# Contacto

- Paulina Pradel (pradel.paulina@gmail.com)
