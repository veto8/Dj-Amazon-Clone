from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from utiles.generate_code import genrate_code



class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(_("Email"), max_length=200 ,blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to='profile/' ,blank=True, null=True)
    code = models.CharField(_("Code"), max_length=50, default=genrate_code)

    def __str__(self):
        return str(self.user)
    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user = instance,
        )



PHONE_TITLE =(
    ('Secondary','Secondary'),
    ('Primary','Primary'),
)
class PhoneNum(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_phone')
    title = models.CharField(_("Title"), max_length=50, choices=PHONE_TITLE)
    number = models.PositiveIntegerField(_("Number"))

    def __str__(self):
        return str(self.user)




ADDRESS_TITLE =(
    ('Home','Home'),
    ('Office','Office'),
    ('Busseniss','Busseniss'),
    ('Academy','Academy'),
    ('Other','Other'),
)
class Address(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address')
    title = models.CharField(_("Title"), max_length=50, choices=ADDRESS_TITLE)
    address = models.PositiveIntegerField(_("Number"))
    notes = models.TextField(_("Notes"),blank=True, null=True)

    def __str__(self):
        return str(self.user)