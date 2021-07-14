from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

# import os
# import tempfile
# from PIL import Image

from .object import BaseObject


__all__ = ['BaseScene']


class BaseScene(object):
    """A base class for all CAD scenes.

    Attributes
    ----------
    objects : dict
        Mapping between object identifiers and objects added to the scene.
        The identifiers are automatically generated and assigned.

    """

    def __init__(self, viewmode=None, fov=None, eye=None, target=None, db=None, depth=10, settings=None):
        self._current = -1
        self._depth = depth
        self._db = db
        self.objects = {}
        self.viewmode = viewmode
        self.fov = fov
        self.eye = eye
        self.target = target
        self.settings = settings or {}

    def add(self, item, name=None, visible=True, **kwargs):
        """Add an object to the scene matching the provided item.

        Parameters
        ----------
        item : :class:`compas.base.Base`
        name : str, optional
        visible : bool, optional

        Returns
        -------
        :class:`compas.scene.BaseObject`
            The created object.
        """
        obj = BaseObject.build(item, scene=self, name=name, visible=visible, **kwargs)
        self.objects[obj.uuid] = obj
        return obj

    def remove(self, item):
        """Remove all objects corresponding to a given data item.

        Parameters
        ----------
        item : :class:`compas.data.Data`
            A data object.
        """
        for uuid in list(self.objects.keys()):
            obj = self.objects[uuid]
            if obj._item is item:
                obj.clear()
                del self.objects[uuid]

    def find(self, item):
        """Find the object corresponding to a given data item.

        Parameters
        ----------
        item : :class:`compas.data.Data`
            A data object.

        Returns
        -------
        :class:`compas.scene.BaseObject`

        Notes
        -----
        There might be multiple scene objects
        """
        for uuid in self.objects:
            obj = self.objects[uuid]
            if obj._item is item:
                return obj

    def find_by_id(self, uuid):
        """Find an object using its UUID.

        Parameters
        ----------
        uuid : str

        Returns
        -------
        :class:`compas.scene.BaseObject`
        """
        if uuid in self.objects:
            return self.objects[uuid]

    def find_by_name(self, name):
        """Find an object using its name.

        Parameters
        ----------
        name : str

        Returns
        -------
        list of :class:`compas.scene.BaseObject`
        """
        objects = []
        for obj in self.objects.values():
            if obj.name == name:
                objects.append(obj)
        return objects

    # abstract methods
    # would be cool to use ABCs
    # but not possible because of ipy bug

    def purge(self):
        """Clear all objects from the scene and remove the underlying data entirely."""
        raise NotImplementedError

    def clear(self):
        """Clear all objects from the scene."""
        raise NotImplementedError

    def draw(self, pause=None):
        """Draw all objects in the scene."""
        raise NotImplementedError

    def update(self, pause=None):
        """Update the display state of all objects in the scene."""
        raise NotImplementedError

    def save(self, filename):
        """Save the scene."""
        raise NotImplementedError

    def undo(self):
        """Undo scene updates."""
        raise NotImplementedError

    def redo(self):
        """Redo scene updates."""
        raise NotImplementedError

    def synchronize(self):
        """Synchronize all data items with the current state of the scene objects."""
        raise NotImplementedError

    def on(self, interval=None, frames=None, record=False, recording=None, dpi=150):
        """Method for decorating callback functions in dynamic visualisations."""
        raise NotImplementedError
