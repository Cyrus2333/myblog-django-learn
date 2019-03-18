from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default="还没想好标题…")
    content = models.TextField()

    def __str__(self):
        return self.title
