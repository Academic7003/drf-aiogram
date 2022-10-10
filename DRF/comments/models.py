from curses import def_shell_mode
from datetime import datetime
from email.policy import default
from django.db import models
from uuid import uuid4

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'photos_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class DirectionModel(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'
class JobModel(models.Model):
    name = models.TextField()
    direction = models.ForeignKey(DirectionModel, related_name='staff', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}'


class UserModel(models.Model):
    user_id = models.IntegerField()
    # user_photo = models.ImageField(upload_to=upload_location, null=True, blank=True)
    photo_id = models.TextField(null=True, blank=True, default='AgACAgIAAxkBAAIKR2MauaF0hSSG1-dy9mY9I1XvxvWhAALUvjEbkZjRSDADYKmMGabgAQADAgADeQADKQQ')
    full_name = models.TextField()
    user_job = models.ForeignKey(JobModel, related_name='staff', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return f'{self.user_id} - {self.full_name} - {self.user_job}'


class RatingModel(models.Model):
    ratinger = models.IntegerField()  # raiting qoyayotgan odam user_id
    whos_rating = models.IntegerField()  # raiting olayotgan odam  user_id
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.ratinger} - {self.whos_rating} - {self.rating}'

class RatingerModel(models.Model):
    user_id = models.IntegerField()
    language = models.TextField(max_length=2, null=True, blank=True, default='ru')
    phone_number = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return f'{self.user_id} - {self.language} - {self.phone_number}'



