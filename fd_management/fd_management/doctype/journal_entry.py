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
    if frappe.db.exists("FD Management", {"reference_jv": self.name}):
        fd_doc = frappe.get_doc('FD Management',{'reference_jv': self.name})
        try:
           fd_doc.cancel()
        except Exception as e:
            frappe.throw(str(e))
        else:
            url = get_url_to_form("FD Management",fd_doc.name)
            frappe.msgprint("FD Management - <a href='{url}'>{doc}</a> is Cancelled".format(url=url, doc=frappe.bold(fd_doc.name)))