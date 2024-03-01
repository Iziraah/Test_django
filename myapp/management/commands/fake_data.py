from django.core.management.base import BaseCommand
from myapp.models import Author, Product, Lesson


class Command(BaseCommand):
    help = "Generate fake authors, products, and lessons."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of authors to generate')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            author = Author(
                first_name =f'Name{i}',
                last_name =f'LastName{i}',
                birth_year = f'2045-02-{i * 2}'
            )
            author.save()

            for j in range(1, count + 1):
                product = Product(
                    name=f'Name{j}',
                    creator=author,
                    cost=j * 9,
                    start_date=f'2045-02-{j:02}' 
                )
                product.save()

                for k in range(count - 5):
                    lesson = Lesson(
                        product=product,
                        name=f'Name{k}',
                        video_url=f'http://some.url{k}'
                    )
                    lesson.save()

        self.stdout.write(self.style.SUCCESS('Successfully created fake data.'))