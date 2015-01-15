==================================
vishap
==================================
Generate embed (HTML) code of services like Youtube or Vimeo from URLs given.
Rules are specified in the plugins.

Comes with plugins for the following services (listed in alphabetical order):

- Vimeo
- Youtube

Installation
==================================
Install with latest stable version from PyPI:

.. code-block:: none

    $ pip install vishap

or install the latest stable version from bitbucket:

.. code-block:: none

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/vishap@stable#egg=vishap

or install the latest stable version from github:

.. code-block:: none

    $ pip install -e git+http://github.org/barseghyanartur/vishap@stable#egg=vishap

That's all. See the `Usage and examples` section for more.

Usage and examples
==================================
Simple usage
----------------------------------
Required imports

.. code-block:: python

    from vishap import render_video

Rendering Vimeo code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following code:

.. code-block:: python

    print render_video('http://vimeo.com/45655450', 500, 281)

Would result the following output:

.. code-block:: html

    <iframe src="//player.vimeo.com/video/45655450" width="500" height="281"
    frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen>
    </iframe>

Rendering Youtube code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following code:

.. code-block:: python

    print render_video('http://www.youtube.com/watch?v=LIPl7PtGXNI', 560, 315)

Would result the following output:

.. code-block:: html

    <iframe width="560" height="315" src="//www.youtube.com/embed/LIPl7PtGXNI"
    frameborder="0" allowfullscreen></iframe>

Filling available area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want your embed code to fill the available area, render it without
``width`` and ``height`` attributes and place it in a container to which it
shall stretch.

Example:

.. code-block:: python

    s = """<div class="video-wrapper">
    {embed_code}
    </div>""".format(
        embed_code = render_video('http://www.youtube.com/watch?v=LIPl7PtGXNI')
    )

It would then result the following output:

.. code-block:: html

    <iframe src="//www.youtube.com/embed/LIPl7PtGXNI"
    frameborder="0" allowfullscreen></iframe>

Your CSS file should then look similar to the following

.. code-block:: css

    .video-wrapper {
        width: 600px;
        height: 500px;
        padding: 0;
    }
        .video-wrapper iframe {
            position: absolute;
            width: 100%;
            height: 100%;
        }

Register a custom plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    class ExamplePlugin(BaseVideoPlugin):
        uid = "example"
        name = "Example"
        url_pattern = "^(?P<prefix>(http\:\/\/www\.youtube\.com\/watch\?v=)|(http\:\/\/www\.youtube\.com\/v\/)|(http\:\/\/youtu\.be\/))(?P<value>[A-Za-z0-9\-=_]{11})"
        id_pattern = "^(?P<value>[A-Za-z0-9\-=_]{11})"
        thumbnail_pattern = "//img.youtube.com/vi/{0}/{1}.jpg"
        embed_code = """
        <iframe src="//www.youtube.com/embed/{video_id}" {options} frameborder="0" allowfullscreen></iframe>
        """

    plugin_registry.register(ExamplePlugin)

Replacing existing plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want to replace/update existing plugin, you can force register it in
the registry.

.. code-block:: python

    class UpdatedYoutubePlugin(BaseVideoPlugin):
        uid = "youtube"
        name = "Youtube"
        url_pattern = "^(?P<prefix>(http\:\/\/www\.youtube\.com\/watch\?v=)|(http\:\/\/www\.youtube\.com\/v\/)|(http\:\/\/youtu\.be\/))(?P<value>[A-Za-z0-9\-=_]{11})"
        id_pattern = "^(?P<value>[A-Za-z0-9\-=_]{11})"
        thumbnail_pattern = "//img.youtube.com/vi/{0}/{1}.jpg"
        embed_code = """
        <iframe src="//www.youtube.com/embed/{video_id}" {options} frameborder="0" allowfullscreen></iframe>
        """

    plugin_registry.register(UpdatedYoutubePlugin, force=True)

Django integration
==================================
Installation
----------------------------------
Add `vishap.contrib.apps.django.vishap` to `INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'vishap.contrib.apps.django.vishap',
        # ...
    )

Usage
----------------------------------
In your template:

Example #1:

.. code-block:: html

    {% load vishap_tags %}
    {% render_video 'http://www.youtube.com/watch?v=LIPl7PtGXNI' 560 315 as rendered_video_example_1 %}
    {{ rendered_video_example_1|safe }}

Example #2:

.. code-block:: html

    {% load vishap_tags %}
    {% with video_url='http://vimeo.com/41055612' video_width='500' video_height='281' %}
    {% render_video video_url video_width video_height as rendered_video_example_2 %}
    {{ rendered_video_example_2|safe }}
    {% endwith %}

Missing a plugin?
==================================
Missing a plugin for your favourite service? Contribute to the project by
making one and it will appear in a new version (which will be released very
quickly) or request a feature.

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>
