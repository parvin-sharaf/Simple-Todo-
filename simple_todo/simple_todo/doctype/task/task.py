import frappe
from frappe.model.document import Document

class Task(Document):
    def validate(self):
        if self.due_date and self.due_date < frappe.utils.today():
            frappe.throw("Due date cannot be in the past")
    
    def on_update(self):
        if self.is_completed:
            frappe.msgprint(f"Task '{self.title}' marked as completed!")