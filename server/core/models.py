from django.db import models


class Link(models.Model):
    url = models.URLField()
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
