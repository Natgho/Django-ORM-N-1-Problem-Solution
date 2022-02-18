from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment = models.TextField()
