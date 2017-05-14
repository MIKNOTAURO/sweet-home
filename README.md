# Plataforma para buscar tu hogar ideal

Pasos para reproducir este proyecto en local

* Instalar PostgreSQL
* Ejecutar la siguiente orden en la terminal: **sudo apt install binutils libproj-dev gdal-bin**
* Instalar PostGIS(en Debian/Ubuntu: postgresql-x.x-postgis)
* Crear la base de datos:
  * create database <nombre_de_la_base_de_datos>;
  * create user <nombre_de_usuario> with password '<contraseña_de_usuario>';
  * alter role <nombre_de_usuario> set client_encoding to 'utf-8';
  * grant all privileges on database <nombre_de_la_base_de_datos> to <noombre_de_usuario>; 
* Cambiar en el archivo env.sh las configuraciones para la base de datos local.
* Ejecutar la siguiente instrucción: en la ubicación del archivo env.sh: source env.sh
* Ejecutar las migraciones: python manage.py migrate
* Correr el proyecto: *python manage.py runserver*


Para más información consultar sobre como instalar los requerimientos de la base de datos:
- [Instalar librerías geospaciales](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install/geolibs/)
- [Instalar PostGIS](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install/postgis/)


