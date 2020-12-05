from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Setup"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Company Structure",
					"description": _(""),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Resource Pool",
					"description": _(""),
					"onboard": 1,
				},
                {
                    "type": "doctype",
                    "name": "Key Result Area",
                    "description": _(""),
                    "onboard": 1,
                }
       
			]
        },

        {
            "label": _("Intention"),
            "icon": "fa fa-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Period or Planning Horizon",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Strategic Intent",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Goal or Objective",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Budget",
                    "description": _(""),
                    "onboard": 1,
                }
            ]
		},
            {
            "label": _("Planning"),
            "icon": "fa fa-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Theme or Headline Program",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Initiative or Project",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Feature or Program Increment or Phase",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Capability",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Portfolio",
                    "description": _(""),
                    "onboard": 1,
                }
            ]
        },
            {
            "label": _("Progress"),
            "icon": "fa fa-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Releases and Progress reports",
                    "description": _(""),
                    "onboard": 1,
                },
                                {
                    "type": "doctype",
                    "name": "Risk",
                    "description": _(""),
                    "onboard": 1,
                }
            ]
        }
	]
