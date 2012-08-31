from Products.CMFCore.utils import getToolByName
PROFILEID = 'profile-collective.pfg.norobots:default'

def common(context):  # pragma: no cover
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILEID)
#    setup.runImportStepFromProfile(PROFILEID,
#                                   'jsregistry', run_dependencies=False,
#                                   purge_old=False)
