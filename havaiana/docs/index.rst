.. Havaiana documentation master file, created by
   sphinx-quickstart on Wed Jul 25 21:11:58 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Havaiana's documentation!
=================================

Havaiana is a dynamic web interface for Ojota.

Havaiana is Free Software! you can check the code at http://bitbucket.org/felipelerena/havaiana

How to use it
=======================
.. code-block:: python
   
   import ojota.examples.examples as pkg
   from havaiana import run

   run(pkg)

Screenshots
===========

.. figure:: screenshots/1.png
   :align: center
   :width: 800

   *All the data sources in the package.*

.. figure:: screenshots/2.png
   :align: center
   :width: 800

   *The items in the data source.*

.. figure:: screenshots/3.png
   :align: center
   :width: 800

   *An item detail.*

Installation
============
With easy_install

.. code-block:: bash

    sudo easy_install Havaiana

With pip

.. code-block:: bash

    sudo pip install Havaiana

From source

.. code-block:: bash

    hg clone ssh://hg@bitbucket.org/felipelerena/Havaiana
    sudo python setup.py install

Table of contents
=================
.. toctree::
   :maxdepth: 2

    Read the module documentation <module>

Dependencies
=====================
 * flask
 * Ojota


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

