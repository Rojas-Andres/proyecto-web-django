# proyecto-web-django

Para comenzar el proyecto instalar las librerias necesarias con el siguiente comando:

   - pip install -r  requeriments.txt
   
   - lo que va a realizar ese comando es instalar las librerias que se encuentran en el archivo txt

Para la funcionalidad de la app de contacto se debe de crear el siguiente archivo correo_contrasena_email.txt y colocar el correo y contraseña:
  
  - primera linea -> correo
  
  - segunda linea -> contraseña 
  
  - Este archivo al subirlo al repositorio lo esta ignorando ya que implemente en el .gitignore para que no lo tomara al hacer el push ya que es mi cuenta personal , por otro lado
  el correo colocado debe de tener habilitado una opcion el cual permita el envio de correos mediante aplicaciones no seguras para que la app de django pueda enviar un correo con
  los datos enviados en el formulario

El proyecto esta en postgres verificar settings.py , por lo tanto al realizar las migraciones deben de tener creada
esa base de datos a la cual se esta conectando por otro lado si no desean especificamente que la base de datos se llame
proyecto-web la pueden cambiar en la linea 102 , en mi caso el puerto es 5433 pero generalmente el puerto para postgres
es el 5432 tener eso en cuenta.

Realizar migraciones : 

	- Recordar que deben de estar en el directorio en donde se encuentre el archivo manage.py
	
	- Como pueden observar las migraciones son muy repetitivas y lo unico que cambia es la app 
	  por lo tanto se puede optimizar.

python manage.py makemigrations blog

python manage.py makemigrations contacto

python manage.py makemigrations servicios

python manage.py makemigrations ProyectoWebApp

python manage.py migrate blog

python manage.py migrate contacto

python manage.py migrate servicios

python manage.py migrate ProyectoWebApp

Luego de realizar cada uno de estos pasos se realizaron cosas interesantes en el panel administrativo de django ,
por lo tanto deben de tener una cuenta , la cuenta la crean de la siguiente manera:

	- python manage.py createsuperuser

	- Ese comando les pedira el usuario , email (opcional si no quieren colocarlo solo pulsar enter) y la contraseña

Ya con eso pueden entrar al panel administrativo de django , cuando corran el servidor con el comando

	python manage.py runserver

	- Este les dara una ruta, generalmente es localhost http://127.0.0.1:8000/ , si quieren acceder al panel
	  administrativo es http://127.0.0.1:8000/admin y ya colocan el usuario y contraseña que ya han creado con
	  anterioridad.