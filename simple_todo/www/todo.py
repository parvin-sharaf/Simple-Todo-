import frappe

def get_context(context):
    # Fetch tasks from your Task DocType
    tasks = frappe.db.sql("""
        SELECT name, title, description, is_completed, due_date 
        FROM `tabTask` 
        ORDER BY creation DESC
    """, as_dict=True)
    context.tasks = tasks
    print(tasks,"GGGGGGGGGGGGGGGGGGGGG")
    return context