# tutorial-django
Tutorial backend django Uniandes - Solar energy

### Requerimientos:

##### Necesarios:
* Instalación de GIT
* Instalación de Python (python o python3)
* Instalación de PIP `sudo apt-get -y install python3-pip`
* Instalación de virtualenv `sudo pip3 install virtualenv`

##### Recomendados:
* OS Linux o Mac
* Visual Studio Code (VS code)
* Complementos de VS code:
  * Python
  * Django
  * Material Icon Theme
  * Backet Pair Colorizer
  * Git Graph
* Postman

### Descarga
1. Crear nuevo entorno virtual con cualquier nombre, en este caso djangodev `virtualenv djangodev`
2. Entrar al folder del entorno virtual `cd  djandodev`
3. Activar entorno virtual `source bin/activate`
4. Instalar Django dentro del entorno virtual `pip3 install django`
5. Clonar proyecto dentro del entorno virtual `git clone https://github.com/cczambrano12/tutorial-django.git`, esto crea una nueva carpeta llamada tutorial-django con los archivos del proyecto

### Ejecución
1. Instalar aplicaciones de tercereros que el proyecto necesita
```
pip3 install djangorestframework
pip3 install requests
pip3 install django-cors-headers
```
2. Ubicarse dentro de la carpeta del proyecto tutorial-django
3. Ejecutar migraciones de django para configurar y generar la base de datos
```
python3 manage.py makemigrations
python3 manage.py migrate
```
4. Ejecutar el servidor `python3 manage.py runserver`

### Rutas (endpoints) del servidor
http://127.0.0.1:8000/admin -> aministrador de django

http://127.0.0.1:8000/helloworld -> Mensaje HTML básico holla mundo con hora actual

http://127.0.0.1:8000/helloworld/2008 -> Mensaje HTML de hola mundo con el numero que se pasa dentro de la ruta al final

http://127.0.0.1:8000/helloworld/json/aaaaabbbcc -> Mensaje JSON con datos recibidos en la ruta y el request 

http://127.0.0.1:8000/energy/data -> Consulta todos los registros almacenados en la base de datos

http://127.0.0.1:8000/energy/data/1 -> Consulta el registro en la base de datos con ID igual al número pasado dentro de la ruta al final

http://127.0.0.1:8000/energy/data -> Consulta todos los registros almacenados en la base de datos

http://127.0.0.1:8000/energy/new?lat=40&lon=-105&tilt=15&power=0.3 -> Consulta API externa de NREL, procesa datos y los almacena en Base de datos.
IMPORTANTE: La API de NREL tiene sólo datos de Estados Unidos por lo que si se desean cambiar los valores de Latitud y Longitud se deben seleccionar valores cercanos a los del ejemplo

### Documentación
API de NREL:
* https://developer.nrel.gov/signup/ -> Para registrarse y general KEY propia
* https://developer.nrel.gov/docs/solar/solar-resource-v1/ -> Documentación API que se va a consumir

Documentación Django:
* https://docs.djangoproject.com/en/3.2/


### Estructura GIT del proyecto
![image](https://user-images.githubusercontent.com/67881744/114646709-60a49a80-9ca1-11eb-9cc3-09ef122ce57b.png)
