.. _gs-blender:

*******************************************************************************
Blender
*******************************************************************************

Blender ships with its own embedded version of Python. Therefore, the simplest
(and recommended) way to install COMPAS for Blender is to replace the embedded
Python by the Python of a `conda` environment that already has COMPAS installed.

It is important that the version of Python installed in the `conda` environment matches
the version of Python that was originally shipped with Blender. For Blender 2.83 LTS
the version of the bundled Python is 3.7, and for 2.93 LTS it is 3.9.

.. note::

    To find out which Python is shipped with your Blender installation, just open Blender
    and have a look at the Interactive Python Console that is part of the UI
    under the Scripting tab.


Installation
============

These instructions are for the latest Blender 2.93 LTS which ships with Python 3.9
If you don't have an environment yet with Python 3.9 and COMPAS you can create one with ``conda``.

.. code-block:: bash

    conda config --add channels conda-forge
    conda create -n blender python=3.9 COMPAS --yes

Configuring Blender to use the newly installed environment is slightly different per OS.

.. raw:: html

    <div class="card">
        <div class="card-header">
            <ul class="nav nav-tabs card-header-tabs">
                <li class="nav-item">
                    <a class="nav-link active" data-toggle="tab" href="#replace_python_windows">Windows</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" data-toggle="tab" href="#replace_python_osx">OSX</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" data-toggle="tab" href="#replace_python_linux">Linux</a>
                </li>
            </ul>
        </div>
        <div class="card-body">
            <div class="tab-content">

.. raw:: html

    <div class="tab-pane active" id="replace_python_windows">

.. code-block:: bash

    conda activate blender
    python -m compas_blender.install "%PROGRAMFILES%\\Blender Foundation\\Blender 2.93\\2.93"

Note that the path ``%PROGRAMFILES%\\Blender Foundation\\Blender 2.93\\2.93`` might be different on your system.
Check your Blender installation and change the path accordingly.

.. raw:: html

    </div>
    <div class="tab-pane" id="replace_python_osx">

.. code-block:: bash

    conda activate blender
    python -m compas_blender.install /Applications/blender.app/Contents/Resources/2.93

Note that the path ``/Applications/blender.app/Contents/Resources/2.93`` might be different on your system.
Check your Blender installation and change the path accordingly.

.. raw:: html

    </div>
    <div class="tab-pane" id="replace_python_linux">

.. code-block:: bash

    conda activate blender
    python -m compas_blender.install ~/Blender/2.93

Note that the path ``~/Blender/2.93`` might be different on your system.
Check your Blender installation and change the path accordingly.

.. raw:: html

    </div>

.. raw:: html

    </div>
    </div>
    </div>

On Windows and OSX, if Blender is installed in the default location, you can simply provide the version number.

.. code-block:: bash

    conda activate blender
    python -m compas_blender.install -v 2.93


Add-ons
=======

For some Blender add-ons, not only the version of Python has to match, but also the version of Numpy.
For example, `Sverchok <http://nortikin.github.io/sverchok/>`_, a Grasshopper-type visual programming tool for Blender,
will not work with the version of Numpy included in the latest COMPAS releases, even though Blender will.

In those cases, you can simply revert to an earlier version of Numpy that is still compatible with COMPAS
in the environment you use with Blender. For Sverchok, this would be version ``1.17.5``,
which is the one shipped with Blender originally. To revert simply do

.. code-block:: bash

    conda activate blender
    conda install numpy=1.17.5

Verify setup
============

In Blender, at the interactive Python prompt (>>>) import the following packages

.. code-block:: python

    >>> import compas
    >>> import compas_blender
    >>> import numpy
    >>> import scipy

Install Python packages
=======================

After replacing the embedded version of Python with the one in the virutual
environment, as instructed above, it is not necessary to activate the environment
before using Blender. However, when you want to update the installed packages,
or add more packages, make sure to activate the Blender environment first.
Otherwise, the changes will not have any effect.

.. code-block:: bash

    conda activate blender
    conda install ...

.. note::

    If you want to use blender with a different environment,
    you simply have to activate that environment and follow the same procedure described above.

Start Blender
=============

Blender uses the command window of your system to display error messages and other text output.
On Windows, the output window can be brought to the front directly from the "Window" menu.
On Mac or Linux, you should start Blender from the command line.

By adding the Blender executable to the ``PATH`` variable this is really simple.
Just add the following to your ``.bash_profile`` or ``.bashrc``.

.. raw:: html

    <div class="card">
        <div class="card-header">
            <ul class="nav nav-tabs card-header-tabs">
                <li class="nav-item">
                    <a class="nav-link active" data-toggle="tab" href="#add_blender_to_path_osx">OSX</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" data-toggle="tab" href="#add_blender_to_path_linux">Linux</a>
                </li>
            </ul>
        </div>
        <div class="card-body">
            <div class="tab-content">

.. raw:: html

    <div class="tab-pane active" id="add_blender_to_path_osx">

.. code-block:: bash

    export PATH="/Applications/blender.app/Contents/MacOS:$PATH"

.. raw:: html

    </div>

.. raw:: html

    <div class="tab-pane" id="add_blender_to_path_linux">

.. code-block:: bash

    export PATH="~/Blender/2.83:$PATH"

Note that this path might be different on your system.

.. raw:: html

    </div>

.. raw:: html

    </div>
    </div>
    </div>

After that starting Blender from the command line is much simpler.

.. code-block:: bash

    blender

Scripting Interface
===================

To switch to the scripting interface, simply select the "Scripting" tab of the main window.

The scripting interface has an embedded interactive Python terminal, which is located in the bottom half of the main window on the left.
If COMPAS was successfully installed you can use it to directly access the ``conda`` environment from where the installation was executed.

.. code-block:: python

    >>> import compas
    >>> import compas_blender
    >>> import numpy
    >>> import scipy
    >>> import bpy

The script editor is quite simple but good enough for basic development.
Line numbers and syntax highlighting should be on by default, but if that is not the case,
they can be turned on with toggle buttons at the top right of the area.
Further customisation of the editor appearance is possible by opening the sidebar from the "View" menu of the editor.

Basic Usage
===========

One of the main advantages of working in Blender is that Blender Python is CPython, and not IronPython like in Rhino and Grasshopper.
This means that all cool Python libraries are directly available and do not need to be accessed through remote procedure calls (RPC).
Especially for code that relies heavily on libraries such as Numpy and Scipy this simplifies the development process quite significantly.

.. code-block:: python

    import compas
    import compas_blender
    from compas.datastructures import Mesh
    from compas_blender.artists import MeshArtist

    compas_blender.clear()

    mesh = Mesh.from_ply(compas.get('bunny.ply'))

    artist = MeshArtist(mesh)
    artist.draw_mesh()

Data Blocks
-----------

Something worth explaining is the use of ``compas_blender.clear()`` in this script.
Blender uses (and re-uses) something called "data blocks".
Objects in the scene have instances of these data blocks assigned to them.
Multiple objects can be linked to the same data block.
As a result, simply deleting an object from the scene will delete the object but not the underlying data block.

If you run a script multiple times,
even if you delete the scene objects between consecutive runs,
you will accumulate the data blocks from previous runs and after a while Blender will become very slow.

``compas_blender.clear()`` attempts to clean up not only the scene objects but also the data blocks.
If somehow you still experience a slowdown, restarting Blender will help (all unused data blocks are then automatically removed).

Layers
------

There are no real layers in Blender; at least not like the layers in, for example, Rhino.
Therefore, the Blender artists have no optional ``layer`` parameter and no ``clear_layer`` method.
Instead, objects are grouped in collections, which can be turned on and off in the Blender UI similar to layers in Rhino.

Collections
-----------

Limitations
===========

``compas_blender`` is not yet as well developed as ``compas_rhino`` and ``compas_ghpython``.
For example, COMPAS geometry objects do not yet have a corresponding artist in ``compas_blender``.
Artists are currently only available for data structures and robots.

There is also no official system yet for making custom COMPAS tools in Blender.
Therefore, COMPAS Blender development is somewhat limited to individual scripts.

Known Issues
============

On Windows, Blender sometimes has issues with finding NumPy libraries.
If this is the case, the problem can usually be solved by reinstalling NumPy in your environment using ``pip``.
However, to avoid issues with other packages that were already installed and depend on a specific version of NumPy,
you should install the same version as the one installed originally by ``conda``.

.. code-block:: bash

    python -c "import numpy; print(numpy.__version__)"

If the above is, for example, ``1.20.3``

.. code-block:: bash

    pip install --force-reinstall numpy==1.20.3

Alternatively, you can create a new environment and simply install entire COMPAS using ``pip``.

.. code-block:: bash

    conda create -n blender python=3.9 cython planarity --yes
    conda activate blender
    pip install compas
    python -m compas_blender.install
