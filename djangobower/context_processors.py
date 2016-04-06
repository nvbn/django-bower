# -*- coding: utf-8 -*-
import os.path
import json
import six
from django.conf import settings
from django.utils.datastructures import OrderedSet


def read_mains():
    for component in settings.BOWER_INSTALLED_APPS:
        component = component.split('#')[0]
        try:
            with open(os.path.join(
                    settings.BOWER_COMPONENTS_ROOT,
                    'bower_components',
                    component,
                    'bower.json')) as bower_json:
                main = json.load(bower_json).get('main')
                if isinstance(main, six.string_types):
                    yield '%s/%s' % (component, main)
                elif isinstance(main, list):
                    for m in main:
                        yield '%s/%s' % (component, m)
        except FileNotFoundError:
            continue


def bower_components(request):
    return {
        'bower_components': OrderedSet([main for main in read_mains()]),
    }
