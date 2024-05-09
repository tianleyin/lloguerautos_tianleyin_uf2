# vehicles/management/commands/generate_fake_data.py

from django.core.management.base import BaseCommand
from lloguer.utils import generate_fake_vehicles

class Command(BaseCommand):
    help = 'Generates fake vehicles using Faker'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of vehicles to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        generate_fake_vehicles(count)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} fake vehicles.'))
