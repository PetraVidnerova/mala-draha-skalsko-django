from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    publish = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
