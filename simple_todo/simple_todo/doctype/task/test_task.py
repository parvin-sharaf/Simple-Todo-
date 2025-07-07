import frappe
import unittest

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = frappe.get_doc({
            "doctype": "Task",
            "title": "Test Task",
            "description": "This is a test task"
        })
        task.insert()
        self.assertEqual(task.title, "Test Task")
        task.delete()