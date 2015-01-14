__title__ = 'vishap.exceptions'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'PluginCodeError', 'ImproperlyConfigured', 'PluginNotFound',
    'PluginDetectionError', 'InvalidRegistryItemType'
)

class PluginCodeError(Exception):
    """
    Exception raised when language code is left empty or has incorrect value.
    """

class ImproperlyConfigured(Exception):
    """
    Exception raised when developer didn't configure the code properly.
    """

class PluginNotFound(Exception):
    """
    Exception raised when language pack is not found for the language code
    given.
    """

class PluginDetectionError(Exception):
    """
    Exception raised when language can't be detected for the text given.
    """

class InvalidRegistryItemType(ValueError):
    """
    Raised when an attempt is made to register an item in the registry which
    does not have a proper type.
    """
