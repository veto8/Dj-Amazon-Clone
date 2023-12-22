# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import gettext as _



# class Profile(models.Model):
#     user =models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     email = models.EmailField(_("Email"), max_length=200)
#     image = models.ImageField(_("Image"), upload_to='profile/')

# def __str__(self):
#     return self.email


# PHONE_TITLE =(
#     ('Secondary','Secondary'),
#     ('Primary','Primary'),
# )
# class PhoneNum(models.Model):
#     user =models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_phone')
#     title = models.CharField(_("Title"), max_length=50, choices=PHONE_TITLE)
#     number = models.PositiveIntegerField(_("Number"))



# ADDRESS_TITLE =(
#     ('Home','Home'),
#     ('Office','Office'),
#     ('Busseniss','Busseniss'),
#     ('Academy','Academy'),
#     ('Other','Other'),
# )
# class Address(models.Model):
#     user =models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address')
#     title = models.CharField(_("Title"), max_length=50, choices=ADDRESS_TITLE)
#     address = models.PositiveIntegerField(_("Number"))
#     notes = models.TextField(_("Notes"),blank=True, null=True)