from django.db import models
import django.utils.timezone



class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=500, blank=True)
    file = models.FileField(null=True, blank=False)
    view_Time = models.DateTimeField(null=True, blank=False, default=django.utils.timezone.now)



    def __str__(self):
        return f"{self.name}, {self.email}, {self.topic},{self.body}"


def __str__(self):
    return f"{self.view},{self.time}"

