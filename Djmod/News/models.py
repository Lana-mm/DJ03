from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title