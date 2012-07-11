from Products.CMFCore.utils import getToolByName

def uninstall(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.pfg.norobots:uninstall')
    setup_tool.setBaselineContext('profile-Products.CMFPlone:plone')
    return "Ran all uninstall steps."