# -*- extra stuff goes here -*-

from Products.CMFCore import utils
from Products.Archetypes.atapi import process_types, listTypes

from zope.i18nmessageid import MessageFactory
norobotsMessageFactory = MessageFactory('collective.pfg.norobots')

from collective.pfg.norobots.config import PROJECTNAME, ADD_PERMISSION
from collective.pfg.norobots.field import FormNorobotsField
from collective.pfg.norobots.widget import NorobotsWidget

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = process_types(listTypes(PROJECTNAME),
                                                      PROJECTNAME)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types=content_types,
        permission=ADD_PERMISSION,
        extra_constructors=constructors,
        fti=ftis,
        ).initialize(context)
