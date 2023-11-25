"""Django's command-line utility for administrative tasks."""
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from products.models import Products,ProductReviews,ProductImage,Category,Brand


def create_pdct(n):
    faker = Faker()
    for x in range(n):
        img = []
        Products.objects.create(
            name = faker.name(),
            sku = random.randint(100000,999999),
            price = random.randint(10,500),
            flag = '',
            image = f'product/{img[random.randint(1,5)]}',
            subtitile = faker.sentence(),
            description = faker.text(),
            quantity = random.randint(10,100),
            brand = Brand.objects.all().order_by('?')[0],
            category = Category.objects.all().order_by('?')[0],
            tags = '',
        )

def create_brand(n):
    faker = Faker()
    img = []
    for x in range(n):
        Brand.objects.create(
            name = faker.name(),
            img = f'brandImage/{img[random.randint(1,5)]}',
            category = Category.objects.all().order_by('?')[0],
        )
    

def create_ctg(n):
    faker = Faker()
    for x in range(n):
        Category.objects.create(
            name = faker.name(),
            img = f'categoryImg/{img[random.randint(0,5)]}',
        )