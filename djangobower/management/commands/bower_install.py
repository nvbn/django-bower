from django.conf import settings
from ...bower import bower_adapter
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        bower_adapter.install(settings.BOWER_INSTALLED_APPS, *args)
