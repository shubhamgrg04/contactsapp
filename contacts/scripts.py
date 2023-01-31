from . import models
import string
import random

def populate_user():
    contact = models.Contact(
        first_name = ''.join(random.choices(string.ascii_lowercase, k=20)).capitalize(),
        last_name = ''.join(random.choices(string.ascii_lowercase, k=20)).capitalize(),
        company_name = f"{''.join(random.choices(string.ascii_lowercase, k=10))} Inc.".capitalize(),
        email = f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
        phone = ''.join(random.choices(string.digits, k=12))
    )
    contact.save()

def populate_users(count=0):
    for i in range(count):
        populate_user()
