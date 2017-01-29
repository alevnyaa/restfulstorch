from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from django import forms

class Category(models.Model):
    name_tr = models.CharField('name [tr]', max_length=48)
    name_en = models.CharField('name [en]', max_length=48)

    parent_cat = models.ForeignKey('Category', null=True, blank=True)

    companies = models.ManyToManyField('Company', blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name_tr + "/" + self.name_en

class Company(models.Model):
    creation_time = models.DateField()

    store_code = models.BigIntegerField(unique=True)
    store_name = models.CharField(max_length=48)

    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)

    address = models.TextField()

    primary_phone_number = models.CharField(max_length=11, blank=True, null=True)
    secondary_phone_number = models.CharField(max_length=11, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    website_address = models.CharField(max_length=128, blank=True, null=True)

    contact_name = models.CharField(max_length=30)
    contact_phone_number = models.CharField(max_length=11)
    contact_email_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name_plural = "companies"

WEEKDAYS = [
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
]

class BusinessHours(models.Model):
    store = models.ForeignKey(
        Company
    )
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()

