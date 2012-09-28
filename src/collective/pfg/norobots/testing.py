from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from Products.CMFCore.utils import getToolByName

from collective.pfg.norobots.tests.utils import PLONE_VERSION

class PloneModuleSandboxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML, install the products and call its initialize() function 
        
        import Products.PloneFormGen
        self.loadZCML(package=Products.PloneFormGen)
        z2.installProduct(app, 'Products.PloneFormGen')
        
        import collective.pfg.norobots
        self.loadZCML(package=collective.pfg.norobots)
        z2.installProduct(app, 'collective.pfg.norobots')
        
    def setUpPloneSite(self, portal):
        # Configure the products using the Quick Installer tool 
        portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        portal_quickinstaller.installProducts( ('Products.PloneFormGen',
                                                'collective.pfg.norobots',) )

    def tearDownZope(self, app):
        # Uninstall products
        z2.uninstallProduct(app, 'collective.pfg.norobots')
        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def tearDownPloneSite(self, portal):
        # Unconfigure the products using the Quick Installer tool
        portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        portal_quickinstaller.uninstallProducts( ('collective.pfg.norobots',
                                                  'Products.PloneFormGen',) )

PLONEMODULE_FIXTURE = PloneModuleSandboxLayer()
PLONEMODULE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONEMODULE_FIXTURE, ),
                       name="collective.pfg.norobots:Integration")
NOROBOTS_FUNCTIONNAL_TESTING = \
    FunctionalTesting(bases=(PLONEMODULE_FIXTURE, ),
                      name="collective.pfg.norobots:Integration")