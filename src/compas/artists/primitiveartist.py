from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.utilities import is_color_rgb
from .artist import Artist


class PrimitiveArtist(Artist):
    """Base class for artists for geometry primitives.

    Parameters
    ----------
    primitive: :class:`compas.geometry.Primitive`
        The geometry of the primitive.
    color : tuple[float, float, float], optional
        The RGB components of the base color of the primitive.

    Attributes
    ----------
    primitive : :class:`compas.geometry.Primitive`
        The geometric primitive associated with the artist.
    color : tuple[float, float, float]
        The color of the object.

    Class Attributes
    ----------------
    default_color : tuple[float, float, float]
        The default rgb color value of the primitive.

    """

    default_color = (0, 0, 0)

    def __init__(self, primitive, color=None, **kwargs):
        super(PrimitiveArtist, self).__init__()
        self._primitive = None
        self._color = None
        self.primitive = primitive
        self.color = color

    @property
    def primitive(self):
        return self._primitive

    @primitive.setter
    def primitive(self, primitive):
        self._primitive = primitive

    @property
    def color(self):
        if not self._color:
            self._color = self.default_color
        return self._color

    @color.setter
    def color(self, color):
        if is_color_rgb(color):
            self._color = color
