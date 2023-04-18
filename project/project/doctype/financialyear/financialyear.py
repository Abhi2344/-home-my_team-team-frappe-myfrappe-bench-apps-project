# Copyright (c) 2023, Faris Ansari and contributors
# For license information, please see license.txt

# import frappe
import datetime
from frappe.model.document import Document

class financialyear(Document):
	


# Financial year start and end dates set by Administrator
 finstartdate = datetime.date(2023, 4, 1)
 finenddate = datetime.date(2024, 3, 31)

# Get start date from user or application
finstartdate = datetime.date(2023, 5, 1)
finenddate = datetime.date(2024, 3 ,30)

# Check if start date falls within financial year start and end dates
if finstartdate <= finstartdate <= finenddate:
    # Proceed with desired operation
    print("finStart date is valid.")
else:
    # Prompt user to enter a valid start date
    print("Start date should fall within the financial year start and end dates.")
