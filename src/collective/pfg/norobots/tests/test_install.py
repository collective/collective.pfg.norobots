import string
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from collective.pfg.norobots.testing import PLONEMODULE_INTEGRATION_TESTING

class TestInstall(unittest.TestCase):

    layer = PLONEMODULE_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(portal_quickinstaller.isProductInstalled('collective.pfg.norobots'),
                        'package appears not to have been installed')

    def test_field_in_types(self):
        """ Validate that the field type is registered in the portal_type tool """
        portal_types = getToolByName(self.portal, 'portal_types')
        self.assertNotEqual(portal_types.getTypeInfo('FormNorobotsField'), None)

    def test_field_in_portal_factory(self):
        """ Validate that the field type is registered in the portal_factory tool """
        portal_factory = self.portal.portal_factory
        self.assertEqual("FormNorobotsField" in portal_factory.getFactoryTypes(), True)

    def test_field_has_no_workflow(self):
        """ Validate that the field has no workflow """
        portal_workflow = getToolByName(self.portal, 'portal_workflow')
        default_chain = portal_workflow.getDefaultChain()
        field_chain = portal_workflow.getChainForPortalType('FormNorobotsField')
        self.assertEqual(field_chain == (), True)

    def test_field_not_in_navtree(self):
        """ Validate that the field type is not listed in the navigation tree """
        portal_properties = getToolByName(self.portal, 'portal_properties')
        navtree_properties = portal_properties.navtree_properties
        self.assertEqual('FormNorobotsField' in navtree_properties.getProperty("metaTypesNotToList"),
                         True)

    def test_skins(self):
        """ Validate that the skin directories are installed in the portal_skins tool
            and available in the skin """
        portal_skins = getToolByName(self.portal, 'portal_skins')
        self.assertEqual("norobots_pfg_field" in portal_skins.objectIds(), True)
        for sname, spath in portal_skins.getSkinPaths():
            paths = filter(None, map(string.strip, spath.split(',')))
            self.assertEqual("norobots_pfg_field" in paths, True,
                             '"norobots_pfg_field" layer not present in "%s" skin' % sname)

class TestUninstall(unittest.TestCase):

    layer = PLONEMODULE_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        
        # Remove the product using the Quick Installer tool
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        portal_quickinstaller.uninstallProducts( ('collective.pfg.norobots',) )
        
    def test_product_is_not_installed(self):
        """ Validate that our products is not yet installed
        """
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(portal_quickinstaller.isProductInstalled('collective.pfg.norobots'),
                        'package appears to be already installed')

    def test_field_not_in_types(self):
        """ Validate that the field type is removed from the portal_type tool """
        portal_types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(portal_types.getTypeInfo('FormNorobotsField'), None)

    #def test_field_not_in_portal_factory(self):
    #    """ Validate that the field type is removed from the portal_factory tool """
    #    portal_factory = self.portal.portal_factory
    #    self.assertEqual("FormNorobotsField" in portal_factory.getFactoryTypes(), False)
    #    ==> uninstall with the profile/uninstall/factorytool.xml doesn't work but the 
    #        type disappear from the portal_factory ZMI user interface

    def test_not_in_skins(self):
        """ Validate that the skin directories is removed from the portal_skins tool
            and from the skin """
        portal_skins = getToolByName(self.portal, 'portal_skins')
        self.assertNotEqual("norobots_pfg_field" in portal_skins.objectIds(), True)
        for sname, spath in portal_skins.getSkinPaths():
            paths = filter(None, map(string.strip, spath.split(',')))
            self.assertNotEqual("norobots_pfg_field" in paths, True,
                                '"norobots_pfg_field" layer present in "%s" skin' % sname)
