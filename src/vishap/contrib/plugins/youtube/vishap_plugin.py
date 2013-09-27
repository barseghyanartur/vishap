__title__ = 'vishap.contrib.plugins.youtube.vishap_plugin'
__version__ = '0.1'
__build__ = 0x000001
__author__ = 'Artur Barseghyan'
__all__ = ('VimeoPlugin',)

from vishap.base import BaseVideoPlugin, plugin_registry

class YoutubePlugin(BaseVideoPlugin):
    """
    Youtube plugin.
    """
    uid = "youtube"
    name = "Youtube"
    url_pattern = "^(?P<prefix>(http\:\/\/www\.youtube\.com\/watch\?v=)|(http\:\/\/www\.youtube\.com\/v\/)|(http\:\/\/youtu\.be\/))(?P<value>[A-Za-z0-9\-=_]{11})"
    id_pattern = "^(?P<value>[A-Za-z0-9\-=_]{11})"
    thumbnail_pattern = "//img.youtube.com/vi/{0}/{1}.jpg"
    embed_code = """
    <iframe src="//www.youtube.com/embed/{video_id}" {options} frameborder="0" allowfullscreen></iframe>
    """

plugin_registry.register(YoutubePlugin)
