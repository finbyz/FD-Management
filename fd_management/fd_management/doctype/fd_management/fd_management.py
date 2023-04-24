# Copyright (c) 2023, finbyx and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FdManagement(Document):
    def validate(self):
        if self.matured_amount< self.fd_amount:
            frappe.throw("Matured Amount Can Not be less then  FD Amount")
    def on_submit(self):
        jv = frappe.new_doc("Journal Entry")
        jv.posting_date = self.posting_date
        jv.voucher_type = "Journal Entry"
        jv.company = self.company
        jv.append('accounts', {
            'account': self.bank_account,
            'credit_in_account_currency':self.fd_amount
        })
        jv.append('accounts', {
            'account': self.fd_account,
            'debit_in_account_currency':self.fd_amount
        })  
        jv.save()
        jv.submit()
                
    def on_update_after_submit(self):
        if self.matured == 1 :
            # if self.matured_amount__1 < self.fd_amount:
            #     frappe.throw("Matured Amount Can Not be less then  FD Amount")
            jv = frappe.new_doc("Journal Entry")
            jv.posting_date = self.posting_date
            jv.voucher_type = "Journal Entry"
            jv.company = self.company
            jv.append('accounts', {
                'account': self.bank_account,
                'debit_in_account_currency': self.matured_amount__1
            })
            jv.append('accounts', {
                'account': self.fd_account,
                'credit_in_account_currency':self.fd_amount
            })
            jv.append('accounts', {
                'account': self.interest_account,
                'credit_in_account_currency':self.interest_amount
            })
            jv.save()
            jv.submit()
            # self.db_set("status", "Matured")