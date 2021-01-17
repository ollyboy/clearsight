from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap':False,
		'heatmap_message': _('Heatmap message'),
		'fieldname': 'theme_brief',
		'transactions': [
			{
				'label': _('Project'),
				'items': ['Initiative or Project']
			}
		]
	}
	