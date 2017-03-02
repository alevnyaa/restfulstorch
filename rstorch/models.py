from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name_tr = models.CharField(_('name [tr]'), max_length=48)
    name_en = models.CharField(_('name [en]'), max_length=48)

    parent = models.ForeignKey(
            'Category',
            null=True,
            blank=True,
            verbose_name=_('parent')
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
        return '/'.join([self.parent.__str__(), self.name_en]) if self.parent is not None else self.name_en

    def str_tr(self):
        return '/'.join([self.parent.str_tr(), self.name_tr]) if self.parent is not None else self.name_tr

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

    address = models.TextField(_('address'))

    primary_phone_number = models.CharField(_('primary phone number'), max_length=11, blank=True, null=True)
    secondary_phone_number = models.CharField(_('secondary phone number'), max_length=11, blank=True, null=True)

    email_address = models.EmailField(_('email address'), blank=True, null=True)

    website_address = models.CharField(_('website address'), max_length=128, blank=True, null=True)

    contact_name = models.CharField(_('contact name'), max_length=30)
    contact_phone_number = models.CharField(_('contact phone number'), max_length=11)
    contact_email_address = models.EmailField(_('contact email address'), blank=True, null=True)

    # If close > open, then the same day
    # else if close = open, open for 24 hours till next day
    # else if close < open, then opens today but closes the next
    hours_monday_open = models.TimeField(_('monday opening'), blank=True, null=True)
    hours_monday_close = models.TimeField(_('monday closing'), blank=True, null=True)
    hours_tuesday_open = models.TimeField(_('tuesday opening'), blank=True, null=True)
    hours_tuesday_close = models.TimeField(_('tuesday closing'), blank=True, null=True)
    hours_wednesday_open = models.TimeField(_('wednesday opening'), blank=True, null=True)
    hours_wednesday_close = models.TimeField(_('wednesday closing'), blank=True, null=True)
    hours_thursday_open = models.TimeField(_('thursday opening'), blank=True, null=True)
    hours_thursday_close = models.TimeField(_('thursday closing'), blank=True, null=True)
    hours_friday_open = models.TimeField(_('friday opening'), blank=True, null=True)
    hours_friday_close = models.TimeField(_('friday closing'), blank=True, null=True)
    hours_saturday_open = models.TimeField(_('saturday opening'), blank=True, null=True)
    hours_saturday_close = models.TimeField(_('saturday closing'), blank=True, null=True)
    hours_sunday_open = models.TimeField(_('sunday opening'), blank=True, null=True)
    hours_sunday_close = models.TimeField(_('sunday closing'), blank=True, null=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = _('store')
        verbose_name_plural = _("stores")
