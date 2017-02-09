from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name_tr = models.CharField(_('name [tr]'), max_length=48)
    name_en = models.CharField(_('name [en]'), max_length=48)

    children = models.ManyToManyField(
            'Category',
            null=True,
            blank=True,
            verbose_name=_('subcategory')
    )

    stores = models.ManyToManyField(
            'Store',
            blank=True,
            verbose_name=_('store')
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name_tr + '/' + self.name_en

class Store(models.Model):
    store_code = models.BigIntegerField(
            _('store code'),
            unique=True
    )

    store_name = models.CharField(
            _('store name'),
            max_length=48
    )

    latitude = models.DecimalField(
            _('latitude'),
            max_digits=8,
            decimal_places=6
    )

    longitude = models.DecimalField(
            _('longitude'),
            max_digits=8,
            decimal_places=6
    )

    creation_time = models.DateField(
            _('creation time'),
            auto_now_add=True
    )

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = _('store')
        verbose_name_plural = _("stores")

class StoreDetails(models.Model):
    business_hours = models.ForeignKey(
        'BusinessHours',
        verbose_name=_('business hours')
    )

    address = models.TextField(_('address'))

    primary_phone_number = models.CharField(_('primary phone number'), max_length=11, blank=True, null=True)
    secondary_phone_number = models.CharField(_('secondary phone number'), max_length=11, blank=True, null=True)
    
    email_address = models.EmailField(_('email address'), blank=True, null=True)
    
    website_address = models.CharField(_('website address'), max_length=128, blank=True, null=True)
    
    contact_name = models.CharField(_('contact name'), max_length=30)
    contact_phone_number = models.CharField(_('contact phone number'), max_length=11)
    contact_email_address = models.EmailField(_('contact email address'), blank=True, null=True)

    class Meta:
        verbose_name = _('store details')
        verbose_name_plural = _('store details')


WEEKDAYS = [
  (1, _('Monday')),
  (2, _('Tuesday')),
  (3, _('Wednesday')),
  (4, _('Thursday')),
  (5, _('Friday')),
  (6, _('Saturday')),
  (7, _('Sunday')),
]

class BusinessHours(models.Model):
    weekday = models.IntegerField(
        _('weekday'),
        choices=WEEKDAYS,
        unique=True
    )
    opening_time = models.TimeField(_('opening time'))
    closing_time = models.TimeField(_('closing time'))
    
    class Meta:
        verbose_name = _("business hours")
        verbose_name_plural = _("business hours")
