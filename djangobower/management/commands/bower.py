from ...bower import bower_adapter
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Call bower in components root (%s).' % (bower_adapter._components_root)

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        bower_adapter.call_bower(*args)
