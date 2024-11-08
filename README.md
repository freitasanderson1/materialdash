# Django Material Administration

MaterialDash é uma interface de administração moderna e responsiva para Django, baseada em Material Design. Este projeto é uma continuação da biblioteca [django-material-admin](https://github.com/MaistrenkoAnton/django-material-admin) de [MaistrenkoAnton](https://github.com/MaistrenkoAnton), que foi descontinuada. Com MaterialDash, buscamos revitalizar e expandir as funcionalidades criadas originalmente, oferecendo uma solução mais atualizada e melhorada para os desenvolvedores.

Nosso objetivo é preservar o trabalho feito com o django-material-admin, ao mesmo tempo em que trazemos novos recursos, correções e melhorias, mantendo o foco em simplicidade, usabilidade e uma experiência de usuário consistente com o Material Design. O MaterialDash possibilita personalizações fáceis e traz um painel administrativo elegante, moderno e funcional para os usuários do Django.

![PyPi](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=0.0.22&x2=0)![Python](https://img.shields.io/badge/python-3.4+-blue.svg)![Django](https://img.shields.io/badge/django-2.2+|5.1.2-mediumseagreen.svg)

## [Contribua com o repositório](https://github.com/freitasanderson1/materialdash)

![Login](https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/login.png)

<!--**login**: *admin*

**password**: *123qaz123!A*-->

## Guia de Inicio Rápido

**Instalação:**
```bash
pip install materialdash
```

1. Adicione **materialdash** e **materialdash.admin** à sua configuração `INSTALLED_APPS` e remova ou comente a linha de `django.contrib.admin`:
   - Necessário

   ```python
   INSTALLED_APPS = (
       'materialdash',
       'materialdash.admin',
       'django.contrib.auth',
       ...
   )
   ```

2. Inclua a URLconf do materialdash em seu projeto `urls.py` assim:
   - Necessário

   ```python
   from django.contrib import admin
   from django.urls import path

   urlpatterns = [
       path('admin/', admin.site.urls),
   ]
   ```

3. Registre seus models em `admin.py`.

   ```python
   from django.contrib.admin import ModelAdmin, register
   from persons.models import Person

   @register(Person)
   class PersonAdmin(ModelAdmin):
       list_display = ('name', 'first_name', 'last_name')
   ```

4. Adicione o ícone ao aplicativo em `app.py` e especifique o uso do aplicativo em `__init__.py`.

   Encontre uma lista de ícones em:
   [Materialize CSS Icons](https://materializecss.com/icons.html) (Opcional)

   **`__init__.py`**

   ```python
   default_app_config = 'persons.apps.PersonsConfig'
   ```

   **`apps.py`**

   ```python
   from django.apps import AppConfig

   class PersonsConfig(AppConfig):
       name = 'persons'
       icon_name = 'person'
   ```

5. Adicionar ícone ao `MaterialModelAdmin` em `admin.py`.

   Fontes do nome do ícone do material:

   - [Materialize CSS Icons](https://materializecss.com/icons.html)
   - [Material Icons](https://material.io/resources/icons/?style=baseline) (Opcional)

   ```python
   from django.contrib.admin import ModelAdmin, register
   from persons.models import Person

   @register(Person)
   class MaterialPersonAdmin(ModelAdmin):
       icon_name = 'person'
   ```

6. Adicione configurações do site Admin ao arquivo `settings.py`:

   ```python
   MATERIAL_ADMIN_SITE = {
       'HEADER':  _('Your site header'),  # Cabeçalho do site de administração
       'TITLE':  _('Your site title'),  # Título do site de administração
       'FAVICON':  'path/to/favicon',  # Favicon do site de administração
       'MAIN_BG_COLOR':  'color',  # Cor principal do site de administração
       'MAIN_HOVER_COLOR':  'color',  # Cor principal do foco do site de administração
       'PROFILE_PICTURE':  'path/to/image',  # Foto do perfil do site de administração
       'PROFILE_BG':  'path/to/image',  # Plano de fundo do perfil do site de administração
       'LOGIN_LOGO':  'path/to/image',  # Logotipo do site de administração na página de login
       'LOGOUT_BG':  'path/to/image',  # Plano de fundo nas páginas de login/logout
       'SHOW_THEMES':  True,  # Mostrar botão de temas administrativos
       'TRAY_REVERSE': True,  # Ocultar ferramentas de objeto e linha de envio adicional por padrão
       'NAVBAR_REVERSE': True,  # Ocultar a barra de navegação lateral por padrão
       'SHOW_COUNTS': True, # Mostrar contagens de instâncias para cada modelo
       'APP_ICONS': {
           'sites': 'send',
       },
       'MODEL_ICONS': {
           'site': 'contact_mail',
       }
   }
   ```
