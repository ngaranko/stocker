from rest_framework import serializers

from stocker.images.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image
        fields = ('url', 'title', 'thumb')
