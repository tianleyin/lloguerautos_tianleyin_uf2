# vehicles/utils.py

from faker import Faker
from .models import Automobil

fake = Faker()

def generate_fake_vehicles(n):
    for _ in range(n):
        marca = fake.company()
        model = fake.word()
        matricula = fake.license_plate()
        Automobil.objects.create(marca=marca, model=model, matricula=matricula)
