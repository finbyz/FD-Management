import frappe
from frappe.utils import get_url_to_form

def on_cancel(self, method):
    if frappe.db.exists("Fixed Deposit", {"matured__jv": self.name}):
        fd_doc = frappe.get_doc('Fixed Deposit',{'matured__jv': self.name})
    # fd_doc = frappe.get_doc({'doctype': 'Fixed Deposit','matured__jv': self.name})
        if fd_doc:
            # frappe.db.set_value('Fixed Deposit', {'matured__jv':self.name}, 'matured', 0)
            # frappe.db.set_value('Fixed Deposit', {'matured__jv':self.name}, 'matured__jv', '')
            # fd_doc.db_set('status', 'Running')
            # frappe.db.commit()
            fd_doc.db_set('matured', 0)
            fd_doc.db_set('matured__jv', '')
            fd_doc.db_set('status', 'Running')
    if frappe.db.exists("Fixed Deposit", {"reference_jv": self.name}):
        fd_doc = frappe.get_doc('Fixed Deposit',{'reference_jv': self.name})
        if fd_doc.previous_fd:
            frappe.db.set_value('Fixed Deposit', fd_doc.previous_fd, 'renewal', 0)
            frappe.db.set_value('Fixed Deposit', fd_doc.previous_fd, 'status', 'Padding')
            frappe.db.commit()
        try:
            fd_doc.cancel()
        except Exception as e:
            frappe.throw(str(e))
        else:
            url = get_url_to_form("Fixed Deposit",fd_doc.name)
            frappe.msgprint("Fixed Deposit - <a href='{url}'>{doc}</a> is Cancelled".format(url=url, doc=frappe.bold(fd_doc.name)))