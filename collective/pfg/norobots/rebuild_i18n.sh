#!/bin/sh

# Synchronise the .pot with the templates.
i18ndude rebuild-pot --pot locales/collective.pfg.norobots.pot --merge locales/manual.pot --create collective.pfg.norobots .

# Synchronise the resulting .pot with the .po files
i18ndude sync --pot locales/collective.pfg.norobots.pot locales/*/LC_MESSAGES/collective.pfg.norobots.po