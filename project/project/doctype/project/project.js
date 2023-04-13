// Copyright (c) 2023, Faris Ansari and contributors
// For license information, please see license.txt
frappe.ui.form.on('Project', {
	refresh: function(frm) {
		// Add custom button to create a Project Task
		frm.add_custom_button(__('Create Project Task'), function() {
			frappe.new_doc('Task', {
				project: frm.doc.name,
				subject: __('New Task')
			});
		});

		// Add validation function to ensure expected end date is not before start date
		frm.cscript.validate = function() {
			if (frm.doc.start_date && frm.doc.expected_end_date && new Date(frm.doc.expected_end_date) < new Date(frm.doc.start_date)) {
				frappe.msgprint(__('Expected End date cannot be before start date'));
				validated = false;
			}
		};
	}
});

