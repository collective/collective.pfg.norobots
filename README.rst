===============================================
collective.pfg.norobots
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

``collective.pfg.norobots`` is a ``PloneFormGen`` field using ``collective.z3cform.norobots``.

``collective.z3cform.norobots`` provides a "human" captcha widget based on a list of
question/answer(s).

This captcha can be used : 

    * as a ``plone.app.discussion`` (Plone Discussions) captcha plugin 
    
    * as a ``z3c form`` field
    
    * as a PloneFormGen field with `collective.pfg.norobots`_

Requirements
------------

I have tested this release with :

    * Plone 4.2.1.1 & PloneFormGen 1.7.2 & collective.z3cform.norobots 1.4.2
    
    * Plone 4.1.6 & PloneFormGen 1.7.2 & collective.z3cform.norobots 1.4.2

Screenshot
------------

.. image:: https://github.com/sylvainb/collective.pfg.norobots/raw/master/docs/collective-pfg-norobots-screenshot.png
   :height: 392px
   :width: 552px
   :scale: 100 %
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
	!!! check the buildout config file ``test-plone-base.cfg`` before running !!!
	(collective.pfg.norobots) ln -s test-plone-4.2.x.cfg buildout.cfg
	(collective.pfg.norobots) python bootstrap.py
	(collective.pfg.norobots) bin/buildout
	[...] be patient... [...]
	(collective.pfg.norobots) ./bin/instance fg

Go to http://localhost:8080, add a new Plone Site and install collective.pfg.norobots.

Launch tests::

	(collective.pfg.norobots) ./bin/test -s collective.pfg.norobots

Launch code coverage::

    (collective.pfg.norobots) bin/coverage
    (collective.pfg.norobots) bin/report
    And open with a browser htmlcov/index.html

Credits
-------

* Sylvain Boureliou [sylvainb] - `GitHub <https://github.com/sylvainb>`_ - `Website <http://www.asilax.fr/>`_
* `Planet Makina Corpus <http://www.makina-corpus.org>`_ - `Makina Corpus <http://www.makina-corpus.com>`_
* `Contact us <mailto:python@makina-corpus.org>`_

Source code
-----------

`Source code <https://github.com/sylvainb/collective.pfg.norobots>`_ is hosted on Github.

How to contribute and submit a patch ?
--------------------------------------

`Source code <https://github.com/sylvainb/collective.pfg.norobots>`_ and an `issue tracker <https://github.com/sylvainb/collective.pfg.norobots/issues>`_ is hosted on Github.



