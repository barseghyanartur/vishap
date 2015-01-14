__title__ = 'vishap.contrib.plugins.vimeo.vishap_plugin'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('VimeoPlugin',)

from vishap.base import BaseVideoPlugin, plugin_registry

class VimeoPlugin(BaseVideoPlugin):
    """
    Vimeo plugin.
    """
    uid = "vimeo"
    name = "Vimeo"
    url_pattern = "^(?P<prefix>(http(s)?\:\/\/www\.vimeo\.com\/)|" \
                  "(http(s)?\:\/\/vimeo\.com\/))(?P<value>\d*)"
    id_pattern = "^(?P<value>\d*{11})"
    embed_code = """
    <iframe src="//player.vimeo.com/video/{video_id}" {options} frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    """

plugin_registry.register(VimeoPlugin)
