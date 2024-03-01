
import random
from django.core.management.base import BaseCommand
from myapp.models import User, Lesson

import random
from django.core.management.base import BaseCommand
from myapp.models import User, Lesson

class Command(BaseCommand):
    help = 'Assign lesson access to users'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Assigning lesson access...'))

        # Получите список всех пользователей и уроков
        users = User.objects.all()
        lessons = Lesson.objects.all()

        # Переберите пользователей и добавьте доступы к урокам
        for user in users:
            # Получите случайные 10 уроков
            user_lessons = random.sample(list(lessons), 10)
            
            # Добавьте доступы к урокам для пользователя
            user.lessons_accessed.add(*user_lessons)

        self.stdout.write(self.style.SUCCESS('Lesson access assigned successfully!'))

