from Acquisition import aq_inner

from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent
from zope.component import getMultiAdapter

from Products.CMFCore.permissions import View

from Products.Archetypes.atapi import StringField
from Products.ATContentTypes.content.base import registerATCT

from Products.PloneFormGen.content.fields import FGStringField
from Products.PloneFormGen.content.fieldsBase import BaseFormField
from Products.PloneFormGen.content.fieldsBase import BaseFieldSchemaStringDefault

from collective.pfg.norobots import norobotsMessageFactory as _
from collective.pfg.norobots.config import PROJECTNAME
from collective.pfg.norobots.widget import NorobotsWidget

HIDDEN_FIELDS = [
#    'title',
#    'description',
    'required',
    'hidden',
    'fgTDefault',
    'fgTEnabled',
    'fgDefault',
    'fgTValidator']


def finalizeFormNorobotsFieldSchema(schema):
    
    # overrided in addFormNorobotsField
    schema['title'].default = 'Are you a human ?'
    # overrided in addFormNorobotsField
    schema['description'].default = 'In order to avoid spam, please answer the question below.'
    
    for field in HIDDEN_FIELDS:
        schema[field].widget.visible = {'view': 'invisible',
                                        'edit': 'invisible'}

FormNorobotsFieldSchema = BaseFieldSchemaStringDefault.copy()
finalizeFormNorobotsFieldSchema(FormNorobotsFieldSchema)


def addFormNorobotsField(self, id, **kwargs):
    obj = FormNorobotsField(id)
    notify(ObjectCreatedEvent(obj))
    self._setObject(id, obj)
    obj = self._getOb(id)
    obj.initializeArchetype(**kwargs)
    
    obj.setTitle(obj.translate(_(u'Are you a human ?')))
    obj.setDescription(obj.translate(_(u'In order to avoid spam, please answer the question below.')))
    
    
    notify(ObjectModifiedEvent(obj))
    return obj.getId()


class FormNorobotsField(FGStringField):

    _at_rename_after_creation = True
    schema = FormNorobotsFieldSchema

    def __init__(self, oid, **kwargs):
        """ initialize class """
        BaseFormField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = StringField('fg_string_field',
            searchable=0,
            required=1,
            write_permission=View,
            #validators=('isNorobotsCorrect',),
            widget=NorobotsWidget(),
            )

    def specialValidator(self, value, field, REQUEST, errors):
        """ validate our answer using the collective.z3cform.norobots validator
        """    
        field_name = field.getName()
        
        question_id = REQUEST.get('%s_question_id' % field_name)
        id_check = REQUEST.get('%s_id_check' % field_name)
        
        norobots = getMultiAdapter((self, REQUEST), name='norobots')
        if not norobots.verify(value, question_id, id_check):
            return str('Wrong answer')
        
        return 0
    
registerATCT(FormNorobotsField, PROJECTNAME)
