# Dashboard

## Instalar e iniciar

```bash
$ # Clonar el repositorio Github
$ git clone https://github.com/app-generator/django-dashboard-gradientable.git
$ cd django-dashboard-gradientable
$
$ # Instalación del ambiente virtual (Linux)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Instalar los requerimientos
$ pip3 install -r requirements.txt
$
$ # Crear los modelos de base datos
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Iniciar el servidor
$ python manage.py runserver # Puerto por defecto 8000
$
$
$ # Acceder al sition web en el navagador: http://127.0.0.1:8000/
```

> Nota: Para usar la aplicación debe registrar un nuevo usuario (http://127.0.0.1:8000/register/) y luego ingresar a la aplicación (http://127.0.0.1:8000/login/).

<br /> 

## Estructura del código


```bash
< PROJECT ROOT >
   |
   |-- core/                               # Proyecto
   |    |-- settings.py                    
   |    |-- wsgi.py                        
   |    |-- urls.py                        
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # Archivos CSS y Javascripts
   |    |
   |    |-- templates/                     # Plantillas del proyecto
   |         |
   |         |-- includes/                 # Componentes HTML
   |         |    |-- navigation.html      # Top menu
   |         |    |-- sidebar.html         # Sidebar
   |         |    |-- footer.html          # Footer
   |         |    |-- scripts.html         # Scripts comunes de las páginas
   |         |
   |         |-- layouts/                  # Páginas superiores
   |         |    |-- base-fullscreen.html # Usadas por las páginas de autenticación
   |         |    |-- base.html            # HTML usado por páginas comunes
   |         |
   |         |-- accounts/                 # Páginas de autenticación
   |         |    |-- login.html           # Página de ingreso
   |         |    |-- register.html        # Pàgina de registro
   |         |
   |      index.html                       # Página por defecto
   |     page-404.html                     # Página de error 404
   |     page-500.html                     # Página de error 404 page
   |       *.html                          # Todas las otras páginas HTML
   |
   |-- authentication/                     # Rutas de las páginas de ingreso y registro
   |    |
   |    |-- urls.py                        # URLs de autenticación
   |    |-- views.py                       # Vistas de autenticación
   |    |-- forms.py                       # Formularios de autenticación
   |
   |-- app/                                # Aplicación
   |    |
   |    |-- views.py                       # HTML del servicio de autenticación
   |    |-- urls.py                        # URLs del servicio de autenticación  
   |
   |-- requirements.txt                    # Requerimientos
   |
   |-- .env                                # Configuración de Django
   |-- manage.py                           # Archivo principal del proyecto
   |
   |-- ************************************************************************
```

<br />