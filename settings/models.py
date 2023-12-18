from django.db import models
from django.utils.translation import gettext as _


class Company(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to='CompanyLogo/')
    call_us = models.CharField(_("Call_us"), max_length=50)
    email_us =models.EmailField(_("Email"), max_length=254)
    subtitle =models.TextField(_("Subtitle"), max_length=500)
    face_link = models.URLField(_("Facebook_link"), max_length=200, blank=True, null=True)
    insta_link = models.URLField(_("Instegrame_link"), max_length=200, blank=True, null=True)
    linkedIn_link = models.URLField(_("LinkedIn_link"), max_length=200, blank=True, null=True)
    twet_link = models.URLField(_("Twettir_link"), max_length=200, blank=True, null=True)
    emails = models.TextField(_("Emails"), max_length=200)
    phones = models.TextField(_("Phones"), max_length=200)
    address =models.TextField(_("Location"), max_length=200)
    
    def __str__(self):
        return self.name
    

class DeleveryFee(models.Model):
    fee = models.FloatField(_("Fee"))

    def __str__(self):
        return str(self.fee)