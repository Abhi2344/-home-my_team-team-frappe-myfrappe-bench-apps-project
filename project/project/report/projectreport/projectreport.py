# Copyright (c) 2023, Faris Ansari and contributors
# For license information, please see license.txt




import frappe
from frappe import _, msgprint

def execute(filters=None):
   if not filters: filters = {}

   data, columns = [], []

   columns = get_columns()
   cs_data = get_cs_data(filters)

   if not cs_data:
     msgprint(_('No record found'))
     return columns,cs_data
   
   data=[]
   for d in cs_data:
       row=frappe._dict({
          'project_id': d.project_id,
          'project_title': d.project_title,
          'project_start_date': d.project_start_date,
          'project_expected_end_date': d.project_expected_end_date,
          'total_resources_working_in_the_project': d.total_resources_working_in_the_project,
          'project_status': d.project_status
       })
       data.append(row)

   return columns, data

def get_columns():
    return[
{
'fieldname': 'project_id',
'label': _('Project ID'),
'fieldtype': 'Link',
'options' :'Project'
},
{
'fieldname': 'title_of_the_project',
'label': _('Project Title'),
'fieldtype': 'Link',
'options' :'Project'
},
{
'fieldname': 'start_date',
'label': _('Project Start Date'),
'fieldtype': 'date',
'options' :'Project'

},
{
'fieldname': 'expected_end_date',
'label': _('Project Expected End Date'),
'fieldtype': 'date',
'options' :'Project'
},
{
'fieldname': 'projectresource',
'label':_('Total Resources Working in the Project'),
'fieldtype': 'Table',
'options' :'ProjectTask'
},
{
'fieldname': 'status',
'label': _('Project Status'),
'fieldtype': 'select',
'options' :'ProjectTask'
},
	]

def get_cs_data(filters):
 conditions = get_conditions(filters)
 data = frappe.get_all(
 doctype='Project',
 fields=['project_id', 'title_of_the_project', 'start_date', 'expected_end_date'],
 filters=conditions
)
 return data

def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
     if filters.get(key):
        conditions[key] = value
     return conditions


