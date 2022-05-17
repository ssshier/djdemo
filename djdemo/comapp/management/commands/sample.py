from django.core.management.base import BaseCommand


def sample():
    pass


class Command(BaseCommand):

    help = "sample"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sample()
