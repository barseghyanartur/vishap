__title__ = 'vishap.discover'
__version__ = '0.1'
__build__ = 0x000001
__author__ = 'Artur Barseghyan'
__all__ = ('autodiscover',)

import os

from six import print_

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from vishap.helpers import PROJECT_DIR
from vishap.conf import get_setting

def autodiscover():
    """
    Autodiscovers the plugins in contrib/plugins.
    """
    PLUGINS_DIR = get_setting('PLUGINS_DIR')
    PLUGIN_MODULE_NAME = get_setting('PLUGIN_MODULE_NAME')
    DEBUG = get_setting('DEBUG')

    for app_path in os.listdir(PROJECT_DIR(PLUGINS_DIR)):
        full_app_path = list(PLUGINS_DIR)
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "vishap.{0}.{1}.{2}".format('.'.join(PLUGINS_DIR), app_path, PLUGIN_MODULE_NAME)
                    )
            except ImportError as e:
                if DEBUG:
                    print_(e)
            except Exception as e:
                if DEBUG:
                    print_(e)
        else:
            pass
