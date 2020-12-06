from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': False,
		'heatmap_message': _(''),
		'fieldname': 'initiative_key',
		'transactions': [
			{
				'label': _('Details'),
				'items': ['Feature or Program Increment or Phase']
			}
		]
	}