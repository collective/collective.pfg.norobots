import os
from setuptools import setup, find_packages

version = '1.0dev'

tests_require = ['zope.testing', 'plone.app.testing']

setup(name='collective.pfg.norobots',
      version=version,
      description="collective.pfg.norobots allows to add a collective.z3cform.norobots captcha field to PloneFormGen forms.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone web zope python ploneformgen field captcha',
      author='Sylvain Boureliou [sylvainb]',
      author_email='sylvain.boureliou@gmail.com',
      url='https://github.com/sylvainb/collective.pfg.norobots',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.pfg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot'
          # -*- Extra requirements: -*-
      ],
      tests_require=tests_require,
      extras_require={'test': tests_require},
      test_suite='collective.pfg.norobots.tests.test_docs.test_suite',
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
