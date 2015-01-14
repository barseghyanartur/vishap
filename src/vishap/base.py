__title__ = 'vishap.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseVideoPlugin', 'plugin_registry',)

import re

from six import string_types

from vishap.exceptions import ImproperlyConfigured, InvalidRegistryItemType

mark_safe = lambda s: s

class BaseVideoPlugin(object):
    """
    Base video plugin.
    """
    uid = None
    name = None
    description = None
    url_pattern = None
    id_pattern = None
    thumbnail_pattern = None
    embed_code = None
    width_param_code = 'width="{width}"'
    height_param_code = 'height="{height}"'

    def __init__(self):
        # Making sure all necessary properties are defined.
        for prop in ('uid', 'name', 'url_pattern', 'embed_code', \
                     'width_param_code', 'height_param_code'):
            if not getattr(self, prop):
                raise ImproperlyConfigured(
                    "You should define ``{0}`` property in your ``{1}.{2}`` "
                    "class.".format(
                        prop, self.__class__.__module__, self.__class__.__name__
                        )
                    )

        # Making sure all necessary methods are defined.
        for meth in ('match', 'render'):
            if not callable(getattr(self, meth, None)):
                raise ImproperlyConfigured(
                    "You should define ``{0}`` method in your ``{1}.{2}`` "
                    "class.".format(
                        prop, self.__class__.__module__, self.__class__.__name__
                        )
                    )
        self.regex = re.compile(self.url_pattern)

    def _match(self, url):
        """
        Generic check if URL matches the pattern.

        :param str url:
        :return bool:
        """
        match = self.regex.match(url)
        return match

    def match(self, url):
        """
        Check if URL matches the pattern.

        :param str url:
        :return bool:
        """
        return self._match(url)

    def _render(self, url, width=None, height=None):
        """
        Renders the HTML code of embed video based on from URL given.

        :param str url:
        :param int width:
        :param int height:
        :return str:
        """
        match = self.match(url)
        if match:
            video_id = match.group('value')
            options = []
            if width:
                options.append(self.width_param_code.format(width=width))
            if height:
                options.append(self.height_param_code.format(height=height))
            response = mark_safe(
                self.embed_code.format(
                    video_id = video_id,
                    options = ' '.join(options)
                    )
                )
            return response

        return ''

    def render(self, url, width=None, height=None):
        """
        Renders the HTML code of embed video based on from URL given.

        :param str url:
        :param int width:
        :param int height:
        :return str:
        """
        return self._render(url=url, width=width, height=height)


class BaseRegistry(object):
    """
    Registry of dash plugins. It's essential, that class registered has
    the ``uid`` property.
    """
    type = None

    def __init__(self):
        assert self.type
        self._registry = {}
        self._forced = []

    def register(self, cls, force=False):
        """
        Registers the plugin in the registry.

        :param mixed.
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType("Invalid item type `{0}` for registry "
                                          "`{1}`".format(cls, self.__class__))

        # If item has not been forced yet, add/replace its' value in the
        # registry.
        if force:

            if not cls.uid in self._forced:
                self._registry[cls.uid] = cls
                self._forced.append(cls.uid)
                return True
            else:
                return False

        else:

            if cls.uid in self._registry:
                return False
            else:
                self._registry[cls.uid] = cls
                return True

    def unregister(self, cls):
        uid = None
        # Unregister by ``uid``.
        if isinstance(cls, string_types):
            uid = cls
        elif issubclass(cls, self.type):
            uid = cls.uid
        else:
            raise InvalidRegistryItemType("Invalid item type `{0}` for registry "
                                          "`{1}`".format(cls, self.__class__))

        # Only non-forced items are allowed to be unregistered.
        if uid in self._registry and not uid in self._forced:
            self._registry.pop(uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """
        Gets the given entry from the registry.

        :param str uid:
        :return mixed.
        """
        return self._registry.get(uid, default)


class PluginRegistry(BaseRegistry):
    """
    Plugin registry.
    """
    type = BaseVideoPlugin


# Register plugins by calling plugin_registry.register()
plugin_registry = PluginRegistry()
