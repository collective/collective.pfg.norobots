from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PloneModuleSandboxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.pfg.norobots
        xmlconfig.file('configure.zcml',
                       collective.pfg.norobots,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.pfg.norobots:default')

PLONEMODULE_FIXTURE = PloneModuleSandboxLayer()
PLONEMODULE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONEMODULE_FIXTURE, ),
                       name="PloneModule:Integration")