from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from demo.countries.choices import COUNTRY_TYPES


class Country(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    picture = models.ImageField(_('Picture'), null=True, blank=True)
    population = models.IntegerField(null=True)
    type = models.CharField(_('Type'), choices=COUNTRY_TYPES, max_length=2)
    is_safe = models.BooleanField(default=True)
    created = models.DateField()
    modified = models.DateTimeField()
    time = models.TimeField()

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        db_table = 'country'
        ordering = ('name',)


class Person(models.Model):
    uuid = models.UUIDField(_('UUID number'))
    nationality = models.ForeignKey('countries.Country', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        db_table = 'persons'
