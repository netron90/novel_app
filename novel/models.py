from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    wallet=models.PositiveIntegerField(default=0)
    pass

class Country(models.Model):
    name = models.CharField(max_length=64),
    country_code = models.CharField(max_length=2, default="")

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="town_list")

    def __str__(self):
        return self.name

class Category (models.Model):
    name = models.CharField(max_length=64)
    town = models.ManyToManyField(Town, blank=True, related_name="category_list")

    def __str__(self):
        return self.name

# class Novel(models.Model):
#     name = models.CharField(max_length=64)
#     image_url = models.CharField(max_length=64, default='novel/imgs/Logo1_1_color.svg') 
#     brief_description = models.CharField(max_length=64)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="novel_list")
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="novel_list", default=1)
#     town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name="novel_list", default="Cotonou")
#     status = models.BooleanField(default=False)
#     date_start = models.DateTimeField()
#     date_end = models.DateTimeField(default=timezone.now)
#     location = models.TextField(default='')
#     phone_contact = models.CharField(max_length=64, default='(+229)0000000000')
#     mail_contact = models.EmailField(default='')
#     number = models.PositiveIntegerField(default=1, editable=False)
#     novel_number = models.CharField(max_length=16, blank=True, editable=False)

#     def generate_novel_number(self):
#         # Format: YYYYMMDDNNNNNNNN
#         date_part = self.date_start.strftime('%Y%m%d')
#         number_part = f'{self.number:08d}'  # Zero-padded to 8 digits
#         return f'{date_part}{number_part}'

#     def save(self, *args, **kwargs):
#         if not self.pk:  # Check if the novel is being created
#             today = timezone.now()
#             current_year_month = today.strftime('%Y%m')
#             max_number = Novel.objects.filter(
#                 date_start__year=today.year,
#                 date_start__month=today.month
#             ).aggregate(models.Max('number'))['number__max']
            
#             if max_number is not None:
#                 self.number = max_number + 1
#             else:
#                 self.number = 1

#             self.novel_number = self.generate_novel_number()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name

class Novel(models.Model):
    name = models.CharField(max_length=64)
    brief_description = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="novel_list")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="novel_list", default=1)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name="novel_list", default="Cotonou")
    status = models.BooleanField(default=False)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(default=timezone.now)
    location = models.TextField(default='')
    phone_contact = models.CharField(max_length=64, default='(+229)0000000000')
    mail_contact = models.EmailField(default='')
    # novel_number = models.CharField(max_length=64, unique=True, blank=True)
    novel_number = models.CharField(max_length=64, blank=True)
    number = models.IntegerField(default=0)

    def generate_novel_number(self):
        today = timezone.now()
        return f"{today.strftime('%Y%m%d')}{self.number:08d}"

    def save(self, *args, **kwargs):
        if not self.novel_number:
            self.novel_number = self.generate_novel_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class NovelImage(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='images')
    image_url = models.CharField(max_length=256)
    interval = models.IntegerField(default=5000)  # Interval in milliseconds

    def __str__(self):
        return f"Image for {self.novel.name}"



