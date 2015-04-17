import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    readme = readme.replace('.. code-block:: none', '.. code-block::')
except:
    readme = ''

version = '0.1.5'

install_requires = [
    'six>=1.4.1',
]

try:
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3
except:
    pass

setup(
    name = 'vishap',
    version = version,
    description = ("Generate embed (HTML) code of services like Youtube or "
                   "Vimeo from URLs given. Rules are specified in the "
                   "plugins."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = 'video, youtube, vimeo, video sharing services app',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/vishap',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = install_requires
)
