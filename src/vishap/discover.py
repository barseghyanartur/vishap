__title__ = 'vishap.discover'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)

import os
import logging

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from vishap.helpers import PROJECT_DIR
from vishap.conf import get_setting

logger = logging.getLogger(__name__)

def autodiscover():
    """
    Autodiscovers the plugins in contrib/plugins.
    """
    PLUGINS_DIR = get_setting('PLUGINS_DIR')
    PLUGIN_MODULE_NAME = get_setting('PLUGIN_MODULE_NAME')

    for app_path in os.listdir(PROJECT_DIR(PLUGINS_DIR)):
        full_app_path = list(PLUGINS_DIR)
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "vishap.{0}.{1}.{2}".format(
                        '.'.join(PLUGINS_DIR),
                        app_path,
                        PLUGIN_MODULE_NAME
                        )
                    )
            except ImportError as e:
                logger.debug(str(e))
            except Exception as e:
                logger.debug(str(e))
        else:
            pass
