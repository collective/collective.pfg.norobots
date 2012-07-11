import string
import unittest2 as unittest

from plone.app.testing import login

from Products.CMFCore.utils import getToolByName

from collective.pfg.norobots.field import HIDDEN_FIELDS
from collective.pfg.norobots.widget import NorobotsWidget

from collective.pfg.norobots.testing import PLONEMODULE_INTEGRATION_TESTING

_marker = object()

CAPTCHA_ID_1 = 'norobots_1'

class TestInstall(unittest.TestCase):

    layer = PLONEMODULE_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'collective.pfg.norobots'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_field_in_types(self):
        pt = self.portal.portal_types
        self.assertEqual("FormNorobotsField" in pt.objectIds(), True)

    def test_fied_in_portal_factory(self):
        pf = self.portal.portal_factory
        self.assertEqual("FormNorobotsField" in pf.getFactoryTypes(), True)

    def test_field_workflow(self):
        pw = self.portal.portal_workflow
        default_chain = pw.getDefaultChain()
        cf_chain = pw.getChainForPortalType('FormNorobotsField')
        self.assertEqual(cf_chain == (), True)

    def test_field_not_in_navtree(self):
        navtree = self.portal.portal_properties.navtree_properties
        mtNotToList = navtree.getProperty("metaTypesNotToList")
        self.assertEqual('FormNorobotsField' in mtNotToList, True)

    def test_skins(self):
        ps = self.portal.portal_skins
        self.assertEqual("norobots_pfg_field" in ps.objectIds(), True)
        for sname, spath in ps.getSkinPaths():
            paths = filter(None, map(string.strip, spath.split(',')))
            self.assertEqual("norobots_pfg_field" in paths, True,
                '"norobots_pfg_field" layer not present in "%s" skin' % sname)

"""
class TestCaptchaField(unittest.TestCase):

    layer = PLONEMODULE_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        
        login(self.portal, 'admin')
        self.portal.invokeFactory('Folder', 'folder')
        self.portal.folder.invokeFactory('FormFolder', 'ff1')
        self.ff1 = getattr(self.portal.folder, 'ff1')
        self.ff1.invokeFactory('FormNorobotsField', CAPTCHA_ID_1)

    def test_schema(self):
        cf = getattr(self.ff1, CAPTCHA_ID_1)
        schema = cf.Schema()
        for field in HIDDEN_FIELDS:
            visibility = schema[field].widget.visible
            self.assertEqual(visibility, {'view': 'invisible',
                                          'edit': 'invisible'},
                '"%s" field is not hidden, but %s:' % (field, visibility))

    def test_field(self):
        cf = getattr(self.ff1, CAPTCHA_ID_1)
        fgField = getattr(cf, 'fgField', _marker)
        self.assertNotEqual(fgField, _marker)
        # Test fgField properties
        self.assertEqual(type(fgField), StringField)
        self.assertEqual(bool(fgField.searchable), False)
        self.assertEqual(fgField.write_permission, View)
        self.assertEqual(type(fgField.widget), NorobotsWidget)
"""



