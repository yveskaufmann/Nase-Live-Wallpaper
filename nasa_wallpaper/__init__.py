"""
Nasa Live Wallpaper
~~~~~~~~~~~~~~~~~~~

Is a python script, that fetches NASA Images of the day
and sets one after another as your desktop background.
"""
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import sys

from .wallpaper import live_wallpaper

__title__ = 'Nasa Live Wallpaper'
__version__ = '0.1.0'
__author__ = 'Yves Kaufmann'
__all__ = ['live_wallpaper']


if ['linux', 'win32', 'darwin'].index(sys.platform) == -1:
    raise NotImplementedError(
        'The platform {0} isn\'t supported.'.format(sys.platform)
    )
