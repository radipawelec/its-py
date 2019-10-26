from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Blog(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    post_picture = models.FileField()
    post_picture_alt = models.CharField(max_length=1000, default="Ple")
    post_title = models.CharField(max_length=1000)
    post_text = models.TextField()
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def was_published_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_title
