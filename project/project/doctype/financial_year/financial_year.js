// Copyright (c) 2023, Faris Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on('Financial Year', {
	refresh: function(frm) {
		// Add a custom validation function to the form
		frm.set_custom_validate(function(doc) {
			if (doc.finstartdate) {
				// Check if the start date falls within the financial year
				const isWithinFinancialYear = function(finstartdate) {
					// Define the financial year start and end dates
					const today = new Date();
					const financialYearStart = new Date(today.getFullYear(), 3, 1);
					const financialYearEnd = new Date(today.getFullYear() + 1, 5, 30); 
					
					// Check if the start date falls within the financial year
					return finstartdate >= financialYearStart && finstartdate <= financialYearEnd;
				}
				
				if (!isWithinFinancialYear(new Date(doc.finstartdate))) {
					// If the start date falls outside the financial year, show an error message
					frappe.msgprint(__("Start date should not fall within the current financial year"));
					return false;
				}
			}
		});
	}
});
