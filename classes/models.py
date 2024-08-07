from django.db import models


# anytime you modify the models file, you must make and run migrations

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images', default='profile.png')


    def __str__(self):
        return self.name


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="description")

    def __str__(self):
        return self.name


