from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    location = models.TextField()

    @property
    def thumb(self):
        return self.location
