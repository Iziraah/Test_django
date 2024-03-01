from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com',
        password='secret', age=25)
        user.save()
        self.stdout.write(f'{user}')

