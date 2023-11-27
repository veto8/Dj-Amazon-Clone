"""Django's command-line utility for administrative tasks."""
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from random import randint,uniform
from products.models import Products,ProductReviews,ProductImage,Category,Brand,User


def create_brand(n):
    faker = Faker()
    for _ in range(n):
        Brand.objects.create(
            name = faker.name(),
            img = f'brandImage/brand{randint(1,4)}.png',
            category = Category.objects.all().order_by('?')[0],
        )
    print(f'create {n} brand')

def create_ctg(n):
    faker = Faker()
    for _ in range(n):
        Category.objects.create(
            name = faker.name(),
            img = f'categoryImg/ctg{randint(1,4)}.png',
        )
    print(f'create {n} category')

def create_pdct(n):
    faker = Faker()
    flag = ['New','Feature','Sale']
    for _ in range(n):
        Products.objects.create(
            name = faker.name(),
            sku = randint(100000,999999),
            price = round(uniform(10.55,99.99),2),
            flag = flag[randint(0,2)],
            image = f'product/pdct{randint(1,31)}.png',
            subtitle = faker.text(max_nb_chars = 400),
            description = faker.text(max_nb_chars = 1000),
            quantity = randint(2,100),
            brand = Brand.objects.all().order_by('?')[0],
            category = Category.objects.all().order_by('?')[0],
        )
    print(f'create {n} product')

def create_pdct_img(n):
    faker = Faker()
    for _ in range(n):
        ProductImage.objects.create(
            img = f'product/pdct{randint(1,31)}.png',
            product = Products.objects.all().order_by('?')[0],
        )
    print(f'create {n} p_img')


def create_product_review(n):
    faker = Faker()
    for _ in range(n):
        ProductReviews.objects.create(
            user = User.objects.all().order_by('?')[0],
            product = Products.objects.all().order_by('?')[0],
            feedback = faker.sentence(nb_words=60),
            rate = randint(1,5),
        )
    print(f'create {n} review')

#delete the dummy data
def delete_dummy_data():
    Brand.objects.all().delete()
    Category.objects.all().delete()
    Products.objects.all().delete()  
    ProductImage.objects.all().delete()
    ProductReviews.objects.all().delete() 
    print("Dummy data deleted successfully.")

# delete_dummy_data()



# create_ctg(20)
# create_brand(40)   
# create_pdct(1000)
# create_pdct_img(1300)
# create_product_review(1000)