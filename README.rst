===============================================
collective.pfg.norobots
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

collective.pfg.norobots is an installable Plone module.

Requirements
------------

    * Tested with Plone 4.1.5 (http://plone.org/products/plone)

Screenshot
------------

.. image:: https://github.com/sylvainb/collective.pfg.norobots/raw/master/docs/collective-pfg-norobots-screenshot.png
   :height: 1039px
   :width: 1026px
   :scale: 70 %
   :alt: Screenshot
   :align: center

Installation
------------

Getting the module
~~~~~~~~~~~~~~~~~~~~

Add ``collective.pfg.norobots`` to your ``plone.recipe.zope2instance`` buildout section e.g.::

    [instance]
    ...
    eggs =
        Plone
        ...
        collective.pfg.norobots

Or, you can add it as a dependency on your own product *setup.py*::

    install_requires=[
        ...
        'collective.pfg.norobots',
    ],

Enabling the module
~~~~~~~~~~~~~~~~~~~~

    Install the module from the Add-ons control panel. That's it!

Quickly test ?
~~~~~~~~~~~~~~~~~~~~

Download ``collective.pfg.norobots`` and use ``virtualenv`` and ``buildout`` to test the module::

	easy_install virtualenv
	cd collective.pfg.norobots
	virtualenv .
	source bin/activate
	(collective.pfg.norobots) easy_install zc.buildout 
	!!! check the buildout content before running !!!
	(collective.pfg.norobots) ln -s test-plone-4.1.x.cfg buildout.cfg
	(collective.pfg.norobots) python bootstrap.py
	(collective.pfg.norobots) bin/buildout
	[...] be patient... [...]
	(collective.pfg.norobots) ./bin/instance fg

Go to http://localhost:8080, add a new Plone Site and install collective.pfg.norobots.

Launch tests::

	(collective.pfg.norobots) ./bin/test -s collective.pfg.norobots

Credits
-------

    * Sylvain Boureliou [sylvainb]

