import unittest2 as unittest

from plone.app.testing import login

from zope.component import getUtility
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from collective.z3cform.norobots.browser.interfaces import INorobotsWidgetSettings

from Products.CMFCore.permissions import View
from Products.Archetypes.atapi import StringField
from Products.validation import validation

from z3c.form.testing import TestRequest

from collective.pfg.norobots.testing import PLONEMODULE_INTEGRATION_TESTING
from collective.pfg.norobots.field import HIDDEN_FIELDS
from collective.pfg.norobots.widget import NorobotsWidget

_marker = object()

TEST_MANAGER_ID = 'admin'
CAPTCHA_ID_1 = 'norobots_1'

class TestCaptchaField(unittest.TestCase):

    layer = PLONEMODULE_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        
        # Add a user and login
        acl_users = getToolByName(self.portal, 'acl_users')
        acl_users.userFolderAddUser(TEST_MANAGER_ID, 'secret', ['Manager'], [])
        login(self.portal, TEST_MANAGER_ID)
        
        # Add a folder and a form with a captcha field 
        self.portal.invokeFactory('Folder', 'folder', title=u"Folder 1")
        folder = self.portal['folder']
        
        folder.invokeFactory('FormFolder', 'pfgform', title=u"PFG Form 1")
        self.pfgform = folder['pfgform']
        self.pfgform.invokeFactory('FormNorobotsField', CAPTCHA_ID_1)
        
        # Configure a question in the NorobotsWidgetSetting
        #registry = getUtility(IRegistry)
        #norobots_settings = registry.forInterface(INorobotsWidgetSettings)
        #self.question_1 = u'What is 5+5 ?' # include a non-ascii char
        #self.answer_1 = u'10; ten'
        #self.id_check_1 = 'd18f7fcb669087ae51905a05875e94f3'
        #norobots_settings.questions = (u'%s::%s' % (self.question_1, self.answer_1),)
        
    def test_schema(self):
        cf = getattr(self.pfgform, CAPTCHA_ID_1)
        schema = cf.Schema()
        for field in HIDDEN_FIELDS:
            visibility = schema[field].widget.visible
            self.assertEqual(visibility, {'view': 'invisible',
                                          'edit': 'invisible'},
                '"%s" field is not hidden, but %s:' % (field, visibility))
                
    def test_field(self):
        cf = getattr(self.pfgform, CAPTCHA_ID_1)
        fgField = getattr(cf, 'fgField', _marker)
        self.assertNotEqual(fgField, _marker)
        
        # Test fgField properties
        self.assertEqual(type(fgField), StringField)
        self.assertEqual(bool(fgField.searchable), False)
        self.assertEqual(fgField.write_permission, View)
        self.assertEqual(type(fgField.widget), NorobotsWidget)
