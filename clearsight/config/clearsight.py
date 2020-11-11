from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Model"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Project",
					"description": _("Load projects here"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Company Structure",
					"description": _("Add companies and groups here"),
					"onboard": 1,
				},
                                                            {
                                        "type": "doctype",
                                        "name": "Program",
                                        "description": _("Define programs"),
                                        "onboard": 1,
                                },
                                                            {
                                        "type": "doctype",
                                        "name": "Budget",
                                        "description": _("Define budget"),
                                        "onboard": 1,
                                },
                                                            
                                                            {
                                        "type": "doctype",
                                        "name": "Strategic Intent",
                                        "description": _("Define Strategic Intent"),
                                        "onboard": 1,
                                },
                                                            {
                                        "type": "doctype",
                                        "name": "Goal or Objective",
                                        "description": _("Define Goals or Objectives"),
                                        "onboard": 1,
                                }
			]
                },

                {
                        "label": _("Summary"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Finance Resource forcast",
                                        "description": _("Generated summary"),
                                        "onboard": 1,
                                }
                        ]
		}
	]
