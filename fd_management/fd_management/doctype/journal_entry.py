import frappe

def on_cancel(self, method):
    if frappe.db.exists("FD Management", {"matured__jv": self.name}):
        fd_doc = frappe.get_doc('FD Management',{'matured__jv': self.name})
    # fd_doc = frappe.get_doc({'doctype': 'FD Management','matured__jv': self.name})
        if fd_doc:
            # frappe.db.set_value('FD Management', {'matured__jv':self.name}, 'matured', 0)
            # frappe.db.set_value('FD Management', {'matured__jv':self.name}, 'matured__jv', '')
            # fd_doc.db_set('status', 'Running')
            # frappe.db.commit()
            fd_doc.db_set('matured', 0)
            fd_doc.db_set('matured__jv', '')
            fd_doc.db_set('status', 'Running')
