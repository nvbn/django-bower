from django.core.management.base import CommandError


class BowerNotInstalled(CommandError):
    """Custom command error"""

    def __init__(self):
        super(BowerNotInstalled, self).__init__(
            "Bower not installed, read instruction here - http://bower.io/",
        )


class LegacyBowerVersionNotSupported(CommandError):
    """Custom command error"""

    def __init__(self):
        super(LegacyBowerVersionNotSupported, self).__init__(
            "Legacy bower versions not supported, please install bower 1.0+",
        )
