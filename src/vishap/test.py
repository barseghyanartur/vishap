# -*- coding: utf-8 -*-

__title__ = 'vishap.tests'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('VishapTest',)

import unittest
import six
from six import print_

from vishap.conf import set_setting, get_setting, reset_to_defaults_settings
from vishap import defaults
from vishap import get_registered_plugin_uids, render_video
from vishap.base import BaseVideoPlugin, plugin_registry

PRINT_INFO = True
TRACK_TIME = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        print_('\n{0}'.format(func.__name__))
        print_('============================')
        print_('""" {0} """'.format(func.__doc__.strip()))
        print_('----------------------------')
        if result is not None:
            try:
                print_(result)
            except Exception as e:
                print_(result.encode('utf8'))

        if TRACK_TIME:
            print_('done in {0} seconds'.format(timer.duration))

        return result
    return inner


def py2only(func):
    """
    Skips the test on Python 3.
    """
    if six.PY2:
        return func

    def dummy(self, *args, **kwargs):
        pass

    return dummy


class VishapTest(unittest.TestCase):
    """
    Tests of ``vishap.utils.render_video``.
    """
    def setUp(self):
        self.vimeo_urls = (
            'http://vimeo.com/45655450',
        )
        self.youtube_urls = (
            'http://www.youtube.com/watch?v=LIPl7PtGXNI',
            'https://www.youtube.com/watch?v=LIPl7PtGXNI',
        )

        self.rendered_vimeo_embed_codes = (
            """
            <iframe src="//player.vimeo.com/video/45655450" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
            """.strip(),
        )

        self.rendered_vimeo_embed_codes_responsive = (
            """
            <iframe src="//player.vimeo.com/video/45655450"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
            """.strip(),
        )

        self.rendered_youtube_embed_codes = (
            """
            <iframe src="//www.youtube.com/embed/LIPl7PtGXNI" width="560" height="315" frameborder="0" allowfullscreen></iframe>
            """.strip(),
            """
            <iframe src="//www.youtube.com/embed/LIPl7PtGXNI" width="560" height="315" frameborder="0" allowfullscreen></iframe>
            """.strip(),
        )
        self.rendered_youtube_responsive_embed_codes = (
            """
            <iframe src="//www.youtube.com/embed/LIPl7PtGXNI"  frameborder="0" allowfullscreen></iframe>
            """.strip(),
            """
            <iframe src="//www.youtube.com/embed/LIPl7PtGXNI"  frameborder="0" allowfullscreen></iframe>
            """.strip(),
        )
        #reset_to_defaults_settings()

    @print_info
    def test_01_get_available_plugin_uids(self):
        """
        Test ``autodiscover`` and ``get_available_plugin_uids``.
        """
        res = get_registered_plugin_uids()
        res.sort()
        c = ['vimeo', 'youtube']
        c.sort()
        self.assertEqual(res, c)
        return res

    def _test_render_video(self, video_url, rendered_video_embed_code, width, height):
        """
        Test rendering of video.
        """
        res = render_video(video_url, width, height).strip()
        self.assertEqual(res, rendered_video_embed_code)
        return res

    def _test_render_video_responsive(self, video_url, rendered_video_embed_code_responsive):
        """
        Test rendering of video.
        """
        res = render_video(video_url).strip()
        self.assertEqual(res, rendered_video_embed_code_responsive)
        return res

    @print_info
    def test_02_render_vimeo(self):
        """
        Test rendering of Vimeo.
        """
        res = []
        for counter, vimeo_url in enumerate(self.vimeo_urls):
            res.append(self._test_render_video(vimeo_url, \
                                               self.rendered_vimeo_embed_codes[counter],
                                               500,
                                               281))
        return res

    @print_info
    def test_03_render_vimeo_responsive(self):
        """
        Test rendering of Vimeo.
        """
        res = []
        for counter, vimeo_url in enumerate(self.vimeo_urls):
            res.append(self._test_render_video_responsive(vimeo_url, \
                                                          self.rendered_vimeo_embed_codes_responsive[counter]))
        return res

    @print_info
    def test_04_render_youtube(self):
        """
        Test rendering of Youtube.
        """
        res = []
        for counter, youtube_url in enumerate(self.youtube_urls):
            res.append(self._test_render_video(youtube_url, \
                                               self.rendered_youtube_embed_codes[counter],
                                               560,
                                               315))
        return res

    @print_info
    def test_05_render_youtube_responsive(self):
        """
        Test rendering of Youtube responsive.
        """
        res = []
        for counter, youtube_url in enumerate(self.youtube_urls):
            res.append(self._test_render_video_responsive(youtube_url, \
                                                          self.rendered_youtube_responsive_embed_codes[counter]))
        return res

    @print_info
    def test_06_register_custom_plugin(self):
        """
        Test registering of a custom plugin.
        """
        class ExamplePlugin(BaseVideoPlugin):
            """
            Example plugin.
            """
            uid = "example"
            name = "Example"
            url_pattern = "^(?P<prefix>(http\:\/\/www\.youtube\.com\/watch\?v=)|(http\:\/\/www\.youtube\.com\/v\/)|(http\:\/\/youtu\.be\/))(?P<value>[A-Za-z0-9\-=_]{11})"
            id_pattern = "^(?P<value>[A-Za-z0-9\-=_]{11})"
            thumbnail_pattern = "//img.youtube.com/vi/{0}/{1}.jpg"
            embed_code = """
            <iframe src="//www.youtube.com/embed/{video_id}" {options} frameborder="0" allowfullscreen></iframe>
            """

        plugin_registry.register(ExamplePlugin)

        assert 'example' in get_registered_plugin_uids()
        res = render_video(self.youtube_urls[0], plugin_uid='example').strip()
        self.assertEqual(res, self.rendered_youtube_responsive_embed_codes[0])
        return res

    @print_info
    def test_07_register_unregister(self):
        """
        Testing register/unregister.
        """
        from vishap.contrib.plugins.vimeo.vishap_plugin import VimeoPlugin

        class Example2Plugin(BaseVideoPlugin):
            """
            Example plugin.
            """
            uid = "youtube"
            name = "Example with youtube ``uid``"
            url_pattern = "^(?P<prefix>(http\:\/\/www\.youtube\.com\/watch\?v=)|(http\:\/\/www\.youtube\.com\/v\/)|(http\:\/\/youtu\.be\/))(?P<value>[A-Za-z0-9\-=_]{11})"
            id_pattern = "^(?P<value>[A-Za-z0-9\-=_]{11})"
            thumbnail_pattern = "//img.youtube.com/vi/{0}/{1}.jpg"
            embed_code = """
            <iframe src="//www.youtube.com/embed/{video_id}" {options} frameborder="0" allowfullscreen></iframe>
            """

        plugin_registry.register(Example2Plugin)
        # Since key `ru` already exists in the registry it can't be replaced (without force-register).
        res = plugin_registry.register(Example2Plugin)
        self.assertTrue(not res)

        # Now with force-register it can.
        res = plugin_registry.register(Example2Plugin, force=True)
        self.assertTrue(res)

        # Once we have it there and it's forced, we can't register another.
        res = plugin_registry.register(Example2Plugin, force=True)
        self.assertTrue(not res)

        # Unregister non-forced language pack.
        res = plugin_registry.unregister(VimeoPlugin)
        self.assertTrue(res and not VimeoPlugin.uid in get_registered_plugin_uids())

        res = plugin_registry.unregister(Example2Plugin)
        self.assertTrue(not res and Example2Plugin.uid in get_registered_plugin_uids())

    @print_info
    def test_08_override_settings(self):
        """
        Testing settings override.
        """
        def override_settings():
            return get_setting('DEBUG')

        self.assertEqual(defaults.DEBUG, override_settings())

        set_setting('DEBUG', True)

        self.assertEqual(True, override_settings())

        return override_settings()


if __name__ == '__main__':
    unittest.main()
