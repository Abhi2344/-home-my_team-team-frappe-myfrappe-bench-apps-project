// Copyright (c) 2023, Faris Ansari and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Projectreport"] = {
	"filters": [
		{
			"fieldname": "project_id",
			"fieldtype": "Link",
			"label": "Project ID",
			"Options" :"Project"
			
		},
		   {
			"fieldname": "title_of_the_project",
			"fieldtype": "Data",
			"label": "Title of the Project",
			
			
		   },

		   {
			"fieldname": "start_date",
			"fieldtype": "Date",
			"label": "Start Date",
			
		   },
		   {
			"fieldname": "expected_end_date",
			"fieldtype": "Date",
			"in_list_view": 1,
			"label": "Expected End Date",

		   }   






	]
};
