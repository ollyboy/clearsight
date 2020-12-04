frappe.views.calendar["Feature or Program Increment or Phase"] = {
        fields:  ["feature_start_date", "feature_end_date", "feature_status", "feature_title", "latest_percent_done_reported", "initiative_brief", "name"],
        field_map: {
                "start": "feature_start_date",
                "end": "feature_end_date",
                "id": "name",
                "title": "feature_title",
                "allDay": 1,
                "progress": "latest_percent_done_reported",
                "status" : "feature_status"
        },
        gantt: true,
        filters: [
                {
                        "fieldtype": "data",
                        "fieldname": "initiative_brief",
                        "options": "Project",
                        "label": __("Project")
                }
        ],
        get_events_method: "frappe.desk.calendar.get_events"
}