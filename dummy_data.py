"""Django's command-line utility for administrative tasks."""
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from random import randint,uniform
from products.models import Products,ProductReviews,ProductImage,Category,Brand


def create_brand(n):
    faker = Faker()
    img = ['brand1.png','brand2.png','brand3.png','brand4.png']
    for x in range(n):
        Brand.objects.create(
            name = faker.name(),
            img = f'brandImage/{img[randint(0,3)]}',
            category = Category.objects.all().order_by('?')[0],
        )
    print(f'create {n} brand')

def create_ctg(n):
    faker = Faker()
    img = ['ctg1.png','ctg2.png','ctg3.png','ctg4.png']
    for x in range(n):
        Category.objects.create(
            name = faker.name(),
            img = f'categoryImg/{img[randint(0,3)]}',
        )
    print(f'create {n} category')

def create_pdct(n):
    faker = Faker()
    img = ['pdct1.png','pdct2.png','pdct3.png','pdct4.png','pdct5.png','pdct6.png','pdct7.png','pdct8.png','pdct9.png','pdct10.png','pdct11.png']
    flag = ['New','Feature','Sale']
    for x in range(n):
        Products.objects.create(
            name = faker.name(),
            sku = randint(100000,999999),
            price = round(uniform(10.55,99.99),2),
            flag = flag[randint(0,2)],
            image = f'product/{img[randint(0,10)]}',
            subtitle = faker.text(max_nb_chars = 1000),
            description = faker.text(max_nb_chars = 5000),
            quantity = randint(2,100),
            brand = Brand.objects.all().order_by('?')[0],
            category = Category.objects.all().order_by('?')[0],
        )
    print(f'create {n} product')

create_brand(10)   
create_ctg(8)
create_pdct(1500)