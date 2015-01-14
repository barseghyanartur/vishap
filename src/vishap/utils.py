__title__ = 'vishap.utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'render_video', 'ensure_autodiscover', 'get_registered_plugins',
    'get_registered_plugin_uids',
)

#from vishap.exceptions import PluginCodeError, PluginNotFound, PluginDetectionError
from vishap.base import plugin_registry
from vishap.discover import autodiscover

_ = lambda s: s

def ensure_autodiscover():
    """
    Ensures that plugins are autodiscovered.
    """
    if not plugin_registry._registry:
        autodiscover()

def get_registered_plugins():
    """
    Gets a list of registered plugins in a form if tuple (plugin name,
    plugin description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    ensure_autodiscover()

    registered_plugins = []

    for uid, plugin in plugin_registry._registry.items():
        registered_plugins.append((uid, plugin))

    return registered_plugins

def get_registered_plugin_uids():
    """
    Gets a list of registered plugins in a form if tuple (plugin name,
    plugin description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    ensure_autodiscover()

    return [uid for uid, plugin in plugin_registry._registry.items()]

def render_video(url, width=None, height=None, plugin_uid=None):
    """
    Renders the video.

    :param str url:
    :param int width:
    :param int height:
    :param str plugin_uid: Preferred plugin to render to video.
    :return str: Returns empty string on failure.
    """
    # Preferred plugin has been given. Try to render.
    if plugin_uid:
        plugin_cls = plugin_registry.get(plugin_uid)

        if not plugin_cls:
            # TODO: Log warnings
            return ''

        plugin = plugin_cls()
        if plugin.match(url):
            return plugin.render(url=url, width=width, height=height)
        else:
            # TODO: Log warnings
            return ''

    # No preferred plugin has been given. Detect which one shall be used and
    # render.
    for plugin_uid, plugin_cls in get_registered_plugins():
        plugin = plugin_cls()
        if plugin.match(url):
            return plugin.render(url=url, width=width, height=height)

    return ''
