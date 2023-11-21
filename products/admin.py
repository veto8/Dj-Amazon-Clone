from django.contrib import admin
from .models import ProductImage,ProductReviews,Products,Brand,Category


admin.site.register(Products)
admin.site.register(ProductImage)
admin.site.register(ProductReviews)
admin.site.register(Brand)
admin.site.register(Category)


