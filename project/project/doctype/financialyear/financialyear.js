// Copyright (c) 2023, Faris Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on('financialyear', {
	 refresh: function(frm) {

		var finstartdate = new Date("2023-04-01");
		var finenddate = new Date("2024-03-31");
		
		// Start date to validate
		var finstartDate = new Date("2023-07-15");
		
		// Check if start date falls within financial year start and end dates
		if (finstartDate >= finstartDate && finstartDate <= finenddate) {
			console.log("Start date is within the financial year.");
		} else {
			console.log("Start date is outside the financial year.");
		}
		
	    

	}
});
