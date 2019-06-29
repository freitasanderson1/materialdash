## Django Material Administration

![Layout](https://github.com/MaistrenkoAnton/django-material-admin/blob/master/app/demo/screens/login.png)


Still in progress

Deployed version:
http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com/admin/

###### login: admin
###### pass: 123qaz123!A

Quick start
-----------

1. Add "django-material-admin" to your INSTALLED_APPS setting like this:

     .. code-block:: python

        INSTALLED_APPS = (
            ...
            'material',
            'django.contrib.admin',
            ...
        )


2. Include the material templates URLconf in your project urls.py like this:

    .. code-block:: python

        urlpatterns = [
            path('admin/', include('material.urls')),
        ]

3. Extend Admin config from  `MaterialModelAdmin`

    .. code-block:: python

        from material.options import MaterialModelAdmin
        from material.decorators import register

        @register(Person)
        class PersonAdmin(MaterialModelAdmin):
            list_display = ('name', 'first_name', 'last_name')

    or

    .. code-block:: python

        from material.options import MaterialModelAdmin
        from material.sites import site

        class PersonAdmin(MaterialModelAdmin):
            list_display = ('name', 'first_name', 'last_name')

        site.register(User)

4. Add icon to the application in `app.py`
https://materializecss.com/icons.html

    .. code-block:: python

        from django.apps import AppConfig


        class PersonsConfig(AppConfig):
            name = 'persons'
            icon_name = 'person'



### Todo:

1. Fix FK choices
1. Fix inlines.
1. App icons check.
1. Change password card margin fixes.
1. Responsive enhancements.
