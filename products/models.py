from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager

FLAG_OPTION = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
)
class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    sku = models.PositiveIntegerField(_('SKU'))
    price = models.FloatField(_('Price'))
    flag = models.CharField(_("Flag"), max_length=50, choices=FLAG_OPTION)
    subtitle = models.TextField(_('Subtitle'),max_length=1000)
    description = models.TextField(_('Description'),max_length=5000)
    quantity = models.PositiveIntegerField(_('Quantity'))
    brand = models.ForeignKey( 'Brand' ,on_delete=models.SET_NULL, related_name='product_Brand' ,blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name='Category' ,blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Products, verbose_name=_("Product_Image"), on_delete=models.CASCADE)
    img = models.ImageField(_("Product_Image"), upload_to='productImg/')

    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("BrandName"), max_length=100)
    img = models.ImageField(_("BrandImage"),upload_to='brandImage/')

    def __str__(self):
        return self.name


class ProductReviews(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"), related_name='user_review')
    product = models.ForeignKey(Products, on_delete=models.CASCADE , verbose_name=_("Product"), related_name='product_review')
    rate = models.PositiveIntegerField(_("ProductRate"), validators=[MinValueValidator(0),MaxValueValidator(5)])
    feedback = models.TextField(_("Feedback"),max_length=1000)
    created_at = models.DateField(_("Date_time"),default=timezone.now)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(_("Category_Name"),max_length=50)
    img = models.ImageField(_("Category_image"), upload_to='categoryImg/')

    def __str__(self):
        return self.name