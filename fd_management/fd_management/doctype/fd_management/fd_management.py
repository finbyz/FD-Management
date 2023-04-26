# Copyright (c) 2023, finbyx and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_url_to_form
from frappe import utils

class FDManagement(Document):
	def validate(self):
		if self.maturity_amount:
			if self.maturity_amount < self.fd_amount:
				frappe.throw("Matured Amount Can Not be less then  FD Amount")
	def on_submit(self):
		if not self.previous_fd:
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
			try:
				jv.save()
				jv.submit()
			except Exception as e:
				frappe.throw(str(e))
			else:
				url = get_url_to_form("Journal Entry",jv.name)
				frappe.msgprint("Journal Entry - <a href='{url}'>{doc}</a> is created".format(url=url, doc=frappe.bold(jv.name)))
		if self.previous_fd:
			jv = frappe.new_doc("Journal Entry")
			jv.posting_date = self.posting_date
			jv.voucher_type = "Journal Entry"
			jv.company = self.company
			jv.append('accounts', {
				'account': self.fd_account,
				'debit_in_account_currency':self.fd_amount
			})
			jv.append('accounts', {
				'account': self.fd_account,
				'credit_in_account_currency': frappe.db.get_value("FD Management",self.previous_fd,'fd_amount')
			})
			jv.append('accounts', {
				'account': self.interest_account,
				'credit_in_account_currency':frappe.db.get_value("FD Management",self.previous_fd,'renewal_interest_amount')
			})  
			try:
				jv.save()
				jv.submit()
			except Exception as e:
				frappe.throw(str(e))
			else:
				url = get_url_to_form("Journal Entry",jv.name)
				frappe.msgprint("Journal Entry - <a href='{url}'>{doc}</a> is created".format(url=url, doc=frappe.bold(jv.name)))
				
	def on_update_after_submit(self):
		if self.matured == 1 and not self.matured__jv :
			# if self.matured_amount < self.fd_amount:
			#     frappe.throw("Matured Amount Can Not be less then  FD Amount")
			jv = frappe.new_doc("Journal Entry")
			jv.posting_date = self.posting_date
			jv.voucher_type = "Journal Entry"
			jv.company = self.company
			jv.append('accounts', {
				'account': self.bank_account,
				'debit_in_account_currency': self.matured_amount
			})
			jv.append('accounts', {
				'account': self.fd_account,
				'credit_in_account_currency':self.fd_amount
			})
			jv.append('accounts', {
				'account': self.interest_account,
				'credit_in_account_currency':self.interest_amount
			})
			try:
				jv.save()
				jv.submit()
			except Exception as e:
				frappe.throw(str(e))
			else:
				url = get_url_to_form("Journal Entry",jv.name)
				frappe.msgprint("Journal Entry - <a href='{url}'>{doc}</a> is created".format(url=url, doc=frappe.bold(jv.name)))
			frappe.db.set_value('FD Management', self.name, 'matured__jv', jv.name)
			frappe.db.set_value('FD Management', self.name, 'status', 'Matured')
			frappe.db.commit()
			# self.db_set('matured__jv', jv.name)
			# self.db_set('status', 'Matured')
		if self.matured__jv:
			frappe.throw(f"FD is already Matured </br> <b>#{self.matured__jv}</b> ")
		if self.matured == 1 and self.renewal == 1:
			frappe.throw("FD is Not Update Renewal and Matured  at a same time")
		if self.renewal == 1:
			fd = frappe.new_doc("FD Management")
			fd.fd_number = self.fd_number
			fd.company = self.company
			fd.bank_account = self.bank_account
			fd.fd_account = self.fd_account
			fd.interest_account = self.interest_account
			fd.fd_start_date = utils.today()
			fd.fd_amount = self.renewal_amount
			fd.previous_fd = self.name
			try:
				fd.save()
			except Exception as e:
				frappe.throw(str(e))
			else:
				url = get_url_to_form("FD Management",fd.name)
				frappe.msgprint("FD Management - <a href='{url}'>{doc}</a> is created".format(url=url, doc=frappe.bold(fd.name)))
			self.db_set('status', 'Renewal')