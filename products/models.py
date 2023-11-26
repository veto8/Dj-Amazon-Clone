from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify



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
    image = models.ImageField(_("Image"), upload_to='product/')
    subtitle = models.TextField(_('Subtitle'),max_length=1000)
    description = models.TextField(_('Description'),max_length=5000)
    quantity = models.PositiveIntegerField(_('Quantity'))
    brand = models.ForeignKey( 'Brand' ,on_delete=models.SET_NULL, related_name='product_Brand' ,blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name='Category' ,blank=True, null=True)
    tags = TaggableManager()
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs) 

class ProductImage(models.Model):
    product = models.ForeignKey(Products, verbose_name=_("Product_Image"), on_delete=models.CASCADE, related_name='product_img')
    img = models.ImageField(_("Product_Image"), upload_to='productImg/')

    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("BrandName"), max_length=100)
    img = models.ImageField(_("BrandImage"),upload_to='brandImage/')
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name='brand_Category' ,blank=True, null=True)

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
    