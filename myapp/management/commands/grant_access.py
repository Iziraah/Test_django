from django.core.management.base import BaseCommand
from myapp.models import User, Lesson

class Command(BaseCommand):
    help = 'Add lessons access to a user by ID'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID')
        parser.add_argument('lesson_ids', type=int, nargs='+', help='Lesson IDs (space-separated)')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        lesson_ids = kwargs['lesson_ids']

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with ID {user_id} does not exist."))
            return

        lessons_added = 0
        for lesson_id in lesson_ids:
            try:
                lesson = Lesson.objects.get(pk=lesson_id)
                user.lessons_accessed.add(lesson)
                lessons_added += 1
            except Lesson.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Lesson with ID {lesson_id} does not exist."))

        self.stdout.write(self.style.SUCCESS(f"Successfully added access to {lessons_added} lessons for user {user_id}."))