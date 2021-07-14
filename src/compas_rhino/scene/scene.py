from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import time
import compas_rhino

from compas.scene import BaseScene


__all__ = ['Scene']


class Scene(BaseScene):
    """Implementation of the base scene for Rhino.

    Attributes
    ----------
    objects : dict
        Mapping between GUIDs and diagram objects added to the scene.
        The GUIDs are automatically generated and assigned.

    """

    def purge(self):
        """Purge all objects from the scene."""
        compas_rhino.rs.EnableRedraw(False)
        try:
            for guid in list(self.objects.keys()):
                self.objects[guid].clear()
                del self.objects[guid]
        except Exception:
            pass
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def clear(self):
        """Clear all objects from the scene."""
        compas_rhino.rs.EnableRedraw(False)
        try:
            for guid in list(self.objects.keys()):
                self.objects[guid].clear()
        except Exception:
            pass
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def clear_layers(self):
        """Clear all object layers of the scene."""
        compas_rhino.rs.EnableRedraw(False)
        try:
            for guid in list(self.objects.keys()):
                self.objects[guid].clear_layer()
        except Exception:
            pass
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def draw(self, pause=None):
        """Draw all objects currently present in the scene.

        Parameters
        ----------
        pause : float, optional
            The amount of time to pause before executing the update, in seconds.
        """
        if pause:
            time.sleep(pause)
            compas_rhino.wait()
        compas_rhino.rs.EnableRedraw(False)
        for guid in self.objects:
            self.objects[guid].draw()
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def update(self, pause=None):
        """Update the display state of all objects currently present in the scene.

        Parameters
        ----------
        pause : float, optional
            The amount of time to pause before executing the update, in seconds.
        """
        if pause:
            time.sleep(pause)
            compas_rhino.wait()
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def on(self, interval, frames, record=False, recording=None, dpi=150):
        """Method for decorating callback functions in dynamic visualisations.

        Parameters
        ----------
        interval : float
            The interval between function calls, in seconds.
        frames : int
            The number of frames to run.
        record : bool, optional
            Indicate that the frames should be recorded.
        recording : str, optional
            The path to the file where the recording should be stored.
        dpi : int, optional
            The frame resolution of the recording.

        Examples
        --------
        .. code-block:: python

            from compas.geometry import Frame, Box, Translation
            from compas_rhino.scene import Scene

            scene = Scene()

            box = Box(Frame.worldXY(), 1, 1, 1)
            obj = scene.add(box, color=(255, 0, 0))
            scene.draw()

            T = Translation.from_vector([0.1, 0, 0])

            @scene.on(interval=0.1, frames=100)
            def do(frame):
                obj.transform(T)

        """
        if record:
            if not recording:
                raise Exception('Please provide a path for the recording.')

        def outer(func):
            count = 0
            while count < frames:
                time.sleep(interval)
                func(count)
                self.update()
                compas_rhino.wait()
                count += 1

        return outer
