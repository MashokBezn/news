from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
