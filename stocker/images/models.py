import os

import PIL
from django.db import models
from django.conf import settings


class Image(models.Model):
    title = models.CharField(max_length=255)
    location = models.TextField()
    thumbnail = models.TextField()

    @property
    def thumb(self):
        """
        Returns image thumbnail location
        Transforms self.thumbnail into reachable path
        """

    def create_thumbnail(self, force=False):
        """
        Create thumbnail for an image.
        """
        if self.thumb and not force:
            return self.thumb

        root, filename = os.path.split(self.location)
        thumbnail_path = os.path.join(root,
                                      settings.IMAGES_THUMBNAILS_DIR,
                                      filename)

        im = PIL.Image.open(self.location)
        im.thumbnail(settings.IMAGES_THUMBNAILS_SIZE, PIL.Image.ANTIALIAS)
        im.save(thumbnail_path, "JPEG")

        self.thumbnail = thumbnail_path
        self.save()
        return self.thumbnail
