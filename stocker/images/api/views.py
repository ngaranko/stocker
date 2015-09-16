from rest_framework import viewsets

from stocker.images.api.serializers import ImageSerializer
from stocker.images.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
