import random
from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = 'Create 10 fake users with predefined age values'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating 10 fake users...'))

        for i in range(12, 21):
            num = random.randint(1, 100)
            user = User(
                name=f'Name{i}',
                email=f'{i*3}@ya.com',
                password=f'{i*num}qwerty',
                age= (i*num)/5
            )
            user.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake users.'))