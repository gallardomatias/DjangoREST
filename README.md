# DjangoREST
building Web APIs

# Documentación de Django
https://docs.djangoproject.com/en/4.0/

# Django REST framework
https://www.django-rest-framework.org/
# Configuración de compilación
## Crear entorno virtual 
``` bash
# 1-) crear entorno virtual ("venv" es el nombre este puede ser reemplazado por cualquiera)
python -m venv venv

# 2-)Activar el entorno para trabajar
venv\Scripts\activate

# Instalar requerimientos 
pip install -r requirements.txt
```

# Comienzo desde cero 
## Instalar pip
``` bash
# pip es un sistema de gestión de paquetes utilizado para instalar paquetes 
python -m pip install --upgrade pip

#Instala django
pip install django

#Creación de un proyecto ("mysite" es el nombre de la carpeta master, puede ser reemplazo )
#Es necesario estar en la carpeta raiz(mysite) para trabjar con manage.py
django-admin startproject mysite

#Creación de la aplicación ("polls" es el nombre de la aplicacion)
py manage.py startapp polls
```

# Comandos 
``` bash

#Iniciar 
python manage.py runserver

#Crear superuser
python manage.py createsuperuser

#Migraciones

python manage.py makemigrations

python manage.py migrate


#Migrar datos
python manage.py dumpdata > db.json

python manage.py loaddata db.json

#Paquetes instalados en entorno 
pip freeze --local

#Inspecciona la base de datos y coloca las tablas en models.py (\app\models.py es la ruta donde enviaremos las tablas de la BDD a modelos )
python manage.py inspectdb > .\app\models.py
```