# -*- extra stuff goes here -*-
from zope.i18nmessageid import MessageFactory

norobotsMessageFactory = MessageFactory('collective.pfg.norobots')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
