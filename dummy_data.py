import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from faker import Faker
import random
from products.models import Brand, Category, Product

def seed_brands(n): # 20
    fake = Faker()
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png']

    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,6)]}"

        Brand.objects.create(
            name = name,
            image = image
        )
    print(f"Seed {n} Brands")



def seed_categories(n): # 20
    fake = Faker()
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png']

    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,7)]}"

        Category.objects.create(
            name = name,
            image = image
        )
    print(f"Seed {n} Categories")



def seed_products(n):
    fake = Faker()

    flag_type = ['New', 'Feature']
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png']

    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        brand = Brand.objects.get(id=random.randint(1,20))
        price = round(random.uniform(19.99,99.99),2)
        desc = fake.text(max_nb_chars=1000)
        flag = flag_type[random.randint(0,1)]
        category = Category.objects.get(id=random.randint(1,20))
        image = f"Product/{images[random.randint(0,7)]}"

        Product.objects.create(
            name = name,
            sku = sku,
            brand = brand,
            price = price,
            desc = desc,
            flag = flag,
            category = category,
            image = image
        )
    print(f"Seed {n} Products")



# seed_brands(20)
# seed_categories(20)
seed_products(1000)