from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of what this command does'

    def handle(self, *args, **kwargs):
        # Your command logic here
        self.stdout.write(self.style.SUCCESS('Successfully executed custom command'))
