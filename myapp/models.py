from datetime import timezone
from django.db import models



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.DateField()
    
    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}'


class Product(models.Model):
    creator = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Name is {self.name}, Creator is {self.creator}'
    
    def distribute_users_to_groups(self):
        group, created = Group.objects.get_or_create(product=self, name=f"Group for {self.name}")

        users = self.user_set.all()

        if self.start_date > timezone.now():
            self.rearrange_groups(users)
        else:
            self.fill_group(group, users)

    def rearrange_groups(self, users):
        groups = Group.objects.filter(product=self)

        groups = sorted(groups, key=lambda x: x.students.count())

        for user in users:
            target_group = min(groups, key=lambda x: x.students.count())
            if target_group.students.count() < target_group.max_users:
                target_group.students.add(user)

    def fill_group(self, group, users):
        for user in users:
            if group.students.count() < group.max_users:
                group.students.add(user)
    
    
class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_url = models.URLField()
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    lessons_accessed = models.ManyToManyField(Lesson, blank=True)
    
    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age:{self.age}'


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    students = models.ManyToManyField(User, related_name='groups', blank=True)