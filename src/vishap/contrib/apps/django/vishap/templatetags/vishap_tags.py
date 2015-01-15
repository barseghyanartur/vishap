from __future__ import absolute_import

__title__ = 'vishap.contrib.apps.django.vishap.templatetags.vishap_tags'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'RenderVideoNode', 'render_video',
)

from django.template import Library, TemplateSyntaxError, Node

from vishap import render_video as render_video_core

register = Library()

class RenderVideoNode(Node):
    """
    Node for ``render_video`` tag.
    """
    def __init__(self, url, width=None, height=None, as_var=None):
        self.url = url
        self.width = width
        self.height = height
        self.as_var = as_var

    def render(self, context):
        request = context['request']
        url = self.url.resolve(context, True)
        width = self.width.resolve(context, True)
        height = self.height.resolve(context, True)

        rendered_video = render_video_core(url, width, height)

        if self.as_var:
            context[self.as_var] = rendered_video
            return ''
        else:
            return rendered_video


@register.tag
def render_video(parser, token):
    """
    Render the video.

    :syntax:
        {% render_video [url] %}
        {% render_video [url] as [context_var_name] %}
        {% render_video [url] [width] [height] %}
        {% render_video [url] [width] [height] as [context_var_name] %}
    :example:
        {% render_video 'http://www.youtube.com/watch?v=LIPl7PtGXNI' 560 315 as rendered_video %}
        {{ rendered_video|safe }}
    """
    bits = token.contents.split()

    url = None
    width = None
    height = None
    as_var = None

    if 6 == len(bits):
        if 'as' != bits[-2]:
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. "
                "Incorrect number of arguments.".format(bits[0])
                )
        width = parser.compile_filter(bits[2])
        height = parser.compile_filter(bits[3])
        as_var = bits[-1]

    elif 4 == len(bits):
        if 'as' == bits[-2]:
            as_var = bits[-1]
        else:
            width = parser.compile_filter(bits[2])
            height = parser.compile_filter(bits[3])

    elif 2 == len(bits):
        pass

    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. "
            "See docs for valid syntax.".format(bits[0])
            )

    url = parser.compile_filter(bits[1])

    return RenderVideoNode(url=url, width=width, height=height, as_var=as_var)
