from django.core.management.base import CommandError


class BowerNotInstalled(CommandError):
    """Custom command error"""

    def __init__(self):
        super(BowerNotInstalled, self).__init__(
            "Bower not installed, read instruction here - http://bower.io/",
        )
