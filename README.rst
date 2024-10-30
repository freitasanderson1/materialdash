MaterialDash é uma interface de administração moderna e responsiva para Django, baseada em Material Design. Este projeto é uma continuação da biblioteca django-material-admin, que foi descontinuada. Com MaterialDash, buscamos revitalizar e expandir as funcionalidades criadas originalmente, oferecendo uma solução mais atualizada e melhorada para os desenvolvedores.

Nosso objetivo é preservar o trabalho feito com o django-material-admin, ao mesmo tempo em que trazemos novos recursos, correções e melhorias, mantendo o foco em simplicidade, usabilidade e uma experiência de usuário consistente com o Material Design. O MaterialDash possibilita personalizações fáceis e traz um painel administrativo elegante, moderno e funcional para os usuários do Django.

|pypi| |python| |django|

.. .. |build|


.. |pypi| image:: https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=0.0.22&x2=0
    :target: https://pypi.org/project/materialdash/
.. |python| image:: https://img.shields.io/badge/python-3.4+-blue.svg
    :target: https://www.python.org/
.. |django| image:: https://img.shields.io/badge/django-2.2+|5.1.2-mediumseagreen.svg
    :target: https://www.djangoproject.com/ 
.. .. |build| image:: http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com:8080/buildStatus/icon?job=Job1
..    :target: http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com

==============================
Django Material Administration
==============================


.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/login.png

.. **login**: *admin*

.. **pass**: *123qaz123!A*

Guia de Inicio Rápido
-----------

 
**pip install materialdash**

1. Adicione **materialdash** e **materialdash.admin** à sua configuração INSTALLED_APPS em vez de **django.contrib.admin**::
 - Necessário

.. code-block:: python

    INSTALLED_APPS = (
        'materialdash',
        'materialdash.admin',

        'django.contrib.auth',
        ...
    )


2. Inclua a URLconf do materialdash em seu projeto **urls.py** assim:
 - Necessário
.. code-block:: python

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]


3. Registre seus models em **admin.py**.
  
.. code-block:: python

    from django.contrib.admin import ModelAdmin, register


    from persons.models import Person

    @register(Person)
    class PersonAdmin(ModelAdmin):
        list_display = ('name', 'first_name', 'last_name')

4. Adicione o ícone ao aplicativo em **app.py** e especifique o uso do aplicativo em **__init__.py**

Encontre uma lista de icones em:
https://materializecss.com/icons.html
 - Opcional
 
**__init.py__**

.. code-block:: python
    
    default_app_config = 'persons.apps.PersonsConfig'
    
**apps.py**

.. code-block:: python

    from django.apps import AppConfig


    class PersonsConfig(AppConfig):
        name = 'persons'
        icon_name = 'person'


5. Adicionar ícone ao MaterialModelAdmin em **admin.py**

Fontes do nome do ícone do material:

https://materializecss.com/icons.html

https://material.io/resources/icons/?style=baseline

 - Opcional

.. code-block:: python

    from django.contrib.admin import ModelAdmin, register

    from persons.models import Person


    @register(Person)
    class MaterialPersonAdmin(ModelAdmin):
        icon_name = 'person'


6. Adicione configurações do site Admin ao arquivo **settings.py**:

 - Opcional
##########################################################

.. code-block:: python

    MATERIAL_ADMIN_SITE = {
        'HEADER':  _('Your site header'),  # Cabeçalho do site de administração
        'TITLE':  _('Your site title'),  # Título do site de administração
        'FAVICON':  'path/to/favicon',  # Favicon do site de administração (o caminho para o arquivo estático deve ser especificado)
        'MAIN_BG_COLOR':  'color',  # Cor principal do site de administração, a cor CSS deve ser especificada
        'MAIN_HOVER_COLOR':  'color',  # Cor principal do foco do site de administração, a cor CSS deve ser especificada
        'PROFILE_PICTURE':  'path/to/image',  # Foto do perfil do site de administração (o caminho para o arquivo estático deve ser especificado)
        'PROFILE_BG':  'path/to/image',  # Plano de fundo do perfil do site de administração (o caminho para o arquivo estático deve ser especificado)
        'LOGIN_LOGO':  'path/to/image',  # Logotipo do site de administração na página de login (o caminho para o arquivo estático deve ser especificado)
        'LOGOUT_BG':  'path/to/image',  # Plano de fundo do site de administração nas páginas de login/logout (o caminho para o arquivo estático deve ser especificado)
        'SHOW_THEMES':  True,  #  Mostrar botão de temas administrativos padrão
        'TRAY_REVERSE': True,  # Ocultar ferramentas de objeto e linha de envio adicional por padrão
        'NAVBAR_REVERSE': True,  # Ocultar a barra de navegação lateral por padrão
        'SHOW_COUNTS': True, # Mostrar contagens de instâncias para cada modelo
        'APP_ICONS': {  # Defina ícones para apps (em letras minúsculas), incluindo apps de terceiros, {'application_name': 'material_icon_name', ...}
            'sites': 'send',
        },
        'MODEL_ICONS': {  # Defina ícones para models(em letras minúsculas),incluindo models de terceiros, {'model_name': 'material_icon_name', ...}
            'site': 'contact_mail',
        }
    }
##########################################################


==============
Videoaulas:
==============

- PySchool

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/pyself.png
   :target: https://pyschool.tech/lessons/django-material-admin-installation


==================
Instruções de vídeo
==================
|
|
- Instalar Django

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/material1.png
   :target: https://youtu.be/LiTcyD9A1A0
|
|
- Instalar materialdash

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/material2.png
   :target: https://youtu.be/trY492bgNQU
|
|
- Cadastro de modelos para interface de administração de materiais

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/material3.png
   :target: https://youtu.be/_ifWi-a1z6M

