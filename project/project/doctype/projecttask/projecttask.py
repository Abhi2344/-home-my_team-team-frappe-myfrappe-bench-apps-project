# Copyright (c) 2023, Faris Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ProjectTask(Document):
	
	def before_save(self):
         self.task_id=self.name
