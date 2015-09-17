import os
from django.conf import settings
from django.core.management.base import BaseCommand

from stocker.images.models import Image


class Command(BaseCommand):
    help = 'Analyse directory and import images into library'

    def add_arguments(self, parser):
        """
        Register custom argument
        """
        parser.add_argument('directory', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        Go through list of directories and call import_directory for each
        """
        for directory in options['directory']:
            self.import_directory(directory)

    def import_directory(self, directory):
        """
        Walk through directory and import all images
        """
        self.stdout.write('Directory: {}'.format(directory))
        saved_files = 0
        for root, dirs, files in os.walk(directory):
            for f in files:
                self.stdout.write('.', ending='')
                if f.split('.')[-1] in settings.IMAGES_EXTENTIONS:
                    location = os.path.join(root, f)
                    try:
                        Image.objects.get(location=location)
                    except Image.DoesNotExist:
                        image = Image(title=f, location=location)
                        image.save()
                        image.create_thumbnail()
                        saved_files += 1
            self.stdout.write('Done.')
            self.stdout.write('Saved files: {}'.format(saved_files))

        return saved_files
