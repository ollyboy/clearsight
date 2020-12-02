frappe.views.calendar["Feature or Program Increment or Phase"] = {
        field_map: {
                "start": "feature_start_date",
                "end": "feature_end_date",
                "id": "name",
                "title": "feature_title",
                "allDay": 1,
                "progress": "latest_percent_done_reported"
        },
        gantt: true,
        filters: [
                {
                        "fieldtype": "Link",
                        "fieldname": "initiative_brief",
                        "options": "Project",
                        "label": __("Project")
                }
        ],
        get_events_method: "frappe.desk.calendar.get_events"
}