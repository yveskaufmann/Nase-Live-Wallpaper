from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import os

_WALLPAPER_FOLDER = os.sep.join(['wallpapers', 'nasa'])


class BackgroundChangeNotPossible(Exception):
    """
    A exception that indicates an error while setting the
    desktop background image.
    """
    pass

class AbstractLiveWallpaper: 
    """
    Base class for a LiveWallpaper, encapsualtes
    os specific implementations like setting the
    background image.
    """

    def set_image(self, path_to_image):
        """
        Change the desktop background to the specified
        image at the specified path.

        Throws BackgroundChangeNotPossible if the change of the background is
        not possible.
        """
        raise NotImplementedError

    def get_picture_folder(self):
        """
        Retrieves path to the default picture folder of the
        underlying system.
        """
        raise NotImplementedError

    def get_wallpaper_folder(self):
        """
        Retrieve the path to the folder in which the nasa wallpapers are stored.
        """
        wallpaper_path = os.path.join(self.get_picture_folder(), _WALLPAPER_FOLDER)
        
        if not os.path.exists(wallpaper_path):
            os.makedirs(wallpaper_path)
        return wallpaper_path

        
