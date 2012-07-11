from Products.Archetypes.Widget import StringWidget
from Products.Archetypes.Registry import registerWidget

NOROBOTS_MACRO = "norobots_pfg_widget"


class NorobotsWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update({'macro': NOROBOTS_MACRO})


registerWidget(NorobotsWidget,
               title='Norobots widget',
               description=('Renders captcha question and the answer string input',),
               used_for=('collective.pfg.norobots.field.FormNorobotsField',)
              )
