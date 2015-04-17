__title__ = 'vishap'
__version__ = '0.1.5'
__build__ = 0x000006
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'render_video', 'get_registered_plugins',
    'get_registered_plugin_uids', 'ensure_autodiscover'
)

from vishap.utils import (
    render_video, get_registered_plugins, get_registered_plugin_uids,
    ensure_autodiscover
    )
