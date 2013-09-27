__title__ = 'vishap.contrib.plugins.vimeo.vishap_plugin'
__version__ = '0.1'
__build__ = 0x000001
__author__ = 'Artur Barseghyan'
__all__ = ('VimeoPlugin',)

from vishap.base import BaseVideoPlugin, plugin_registry

class VimeoPlugin(BaseVideoPlugin):
    """
    Vimeo plugin.
    """
    uid = "vimeo"
    name = "Vimeo"
    url_pattern = "^(?P<prefix>(http(s)?\:\/\/www\.vimeo\.com\/)|(http(s)?\:\/\/vimeo\.com\/))(?P<value>\d*)"
    id_pattern = "^(?P<value>\d*{11})"
    embed_code = """
    <iframe src="//player.vimeo.com/video/{video_id}" {options} frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    """

plugin_registry.register(VimeoPlugin)
