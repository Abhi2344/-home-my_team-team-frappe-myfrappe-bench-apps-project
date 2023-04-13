# Copyright (c) 2023, Faris Ansari and contributors
# For license information, please see license.txt

# import frappe
import datetime
from frappe.model.document import Document

class financialyear(Document):
	
 def is_within_financial_year(start_date):
    # Define the financial year start and end dates
    financial_year_start = datetime.date.today().replace(month=4, day=1) # July 1st of the current year
    financial_year_end = financial_year_start.replace(year=financial_year_start.year + 1) - datetime.timedelta(days=1) # June 30th of the following year
    
    # Check if the start date falls within the financial year
    if start_date >= financial_year_start and start_date <= financial_year_end:
        return True
    else:
        return False
