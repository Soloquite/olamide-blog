from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__(self):
        return self.title
