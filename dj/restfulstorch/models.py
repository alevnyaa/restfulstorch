from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from django import forms

class Category(models.Model):
    name_tr = models.CharField('name [tr]', max_length=48)
    name_en = models.CharField('name [en]', max_length=48)

    parent_cat = models.ForeignKey('Category', null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name_tr + "/" + self.name_en

class Place(models.Model):
    store_code = models.BigIntegerField(unique=True)
    store_name = models.CharField(max_length=48)

    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)

    address = models.TextField()

    primary_phone_number = models.CharField(max_length=11, blank=True)
    secondary_phone_number = models.CharField(max_length=11, blank=True)
    email_address = models.EmailField(blank=True)
    website_address = models.CharField(max_length=128, blank=True)

    contact_name = models.CharField(max_length=30)
    contact_phone_number = models.CharField(max_length=11)
    contact_email_address = models.EmailField(blank=True)

    #working times all 7 days blank=True

    def __str__(self):
        return self.store_name
