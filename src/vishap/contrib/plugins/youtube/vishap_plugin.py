__title__ = 'vishap.contrib.plugins.youtube.vishap_plugin'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('YoutubePlugin',)

from vishap.base import BaseVideoPlugin, plugin_registry

class YoutubePlugin(BaseVideoPlugin):
    """
    Youtube plugin.
    """
    uid = "youtube"
    name = "Youtube"
    url_pattern = "^(?P<prefix>(https?\:\/\/www\.youtube\.com\/watch\?v=)|" \
                  "(https?\:\/\/www\.youtube\.com\/v\/)|" \
                  "(https?\:\/\/youtu\.be\/))(?P<value>[A-Za-z0-9\-=_]{11})"
    id_pattern = "^(?P<value>[A-Za-z0-9\-=_]{11})"
    thumbnail_pattern = "//img.youtube.com/vi/{0}/{1}.jpg"
    embed_code = """
    <iframe src="//www.youtube.com/embed/{video_id}" {options} frameborder="0" allowfullscreen></iframe>
    """

plugin_registry.register(YoutubePlugin)
