.. Havaiana documentation master file, created by
   sphinx-quickstart on Wed Jul 25 21:11:58 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Havaiana's documentation!
=================================

Havaiana is a dynamic web interface for Ojota (http://ojota.rtfd.org).

Havaiana is Free Software! you can check the code at http://github.com/felipelerena/havaiana

How to use it
=======================
Hello World
___________

.. code-block:: python
   
   import ojota.examples.examples as pkg
   from havaiana import Site

   site = Site(pkg)
   site.serve()

Custom rendering for a field
____________________________

.. code-block:: python
   
    import food_data

    from havaiana import Site

    def ingredients_list(field, item, backwards):
        required = field in item.required_fields
        ingredients = getattr(item, field)
        items = []
        for element in ingredients:
            item = '<li><a href="/Ingredients/%s">%s</a></li>' % (element.primary_key,
                                                        element)
            items.append(item)
        value = "<ul>%s</ul>" %  "".join(items)
        related = False

        return (field, value, required, related)
    if __name__ == "__main__":
        renderers = [('Recipe', 'ingredients', ingredients_list)]
        site = Site(food_data, "My Food Database", renderers)

        site.serve()

Adding a chart on a view
____________________________

.. code-block:: python
      
    import food_data

    from havaiana import Site
    from havaiana.charts import LineChart

    class RainChartView(LineChart):
        def __init__(self):
            LineChart.__init__(self, "Recipes uploaded to the site",
                               "uploads", 800, 400)

        def get_data(self, data):
            keys = []
            points = []
            for element in data:
                keys.append(element.date)
                points.append({"value": int(element.number),
                               "xlink": "/Recipes uploaded by day/%s" % element.date})
            return keys, points

    if __name__ == "__main__":
        renderers = [
            ('RecipesByDay', "__index_chart", RainChartView)
        ]

        site = Site(food_data, "My Food Database", renderers)
        site.serve()


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

.. figure:: screenshots/4.png
   :align: center
   :width: 800

   *Edit an existing element.*

.. figure:: screenshots/5.png
   :align: center
   :width: 800
   
   *Create new element.*

.. figure:: screenshots/6.png
   :align: center
   :width: 800

   *A view with custom rendering.*

.. figure:: screenshots/7.png
   :align: center
   :width: 755

   *You can sort the data.*

.. figure:: screenshots/8.png
   :align: center
   :width: 872

   *Render charts with your data*

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

    git clone git@github.com:felipelerena/havaiana.git
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
 * wtforms
 * pygal

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

