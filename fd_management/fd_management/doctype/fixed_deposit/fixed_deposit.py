# Copyright (c) 2023, finbyx and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_url_to_form
from frappe import utils

class FixedDeposit(Document):
	def validate(self):
		if self.maturity_amount < self.fd_amount:
			frappe.throw("Matured Amount Can Not be less then  FD Amount")
		if self.fd_start_date >= self.matured_date:
			frappe.throw("Matured Date Can Not be less then Or equal FD Start Date")
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
			frappe.db.set_value('Fixed Deposit', self.name, 'reference_jv', jv.name)
			frappe.db.commit()
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
				'credit_in_account_currency': frappe.db.get_value("Fixed Deposit",self.previous_fd,'fd_amount')
			})
			jv.append('accounts', {
				'account': self.interest_account,
				'credit_in_account_currency':frappe.db.get_value("Fixed Deposit",self.previous_fd,'renewal_interest_amount')
			})  
			try:
				jv.save()
				jv.submit()
			except Exception as e:
				frappe.throw(str(e))
			else:
				url = get_url_to_form("Journal Entry",jv.name)
				frappe.msgprint("Journal Entry - <a href='{url}'>{doc}</a> is created".format(url=url, doc=frappe.bold(jv.name)))
			frappe.db.set_value('Fixed Deposit', self.name, 'reference_jv', jv.name)
			frappe.db.set_value('Fixed Deposit', self.previous_fd, 'renewal_jv', jv.name)
			frappe.db.commit()

	def on_update_after_submit(self):
		if self.matured__jv:
			frappe.throw(f"FD is already Matured </br> <b>#{self.matured__jv}</b> ")
		if self.matured == 1 and not self.matured__jv :
			if self.matured_amount < self.fd_amount:
			    frappe.throw("Matured Amount Can Not be less then  FD Amount")
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
			# frappe.db.set_value('Fixed Deposit', self.name, 'matured__jv', jv.name)
			# frappe.db.set_value('Fixed Deposit', self.name, 'status', 'Matured')
			# frappe.db.commit()
			self.db_set('matured__jv', jv.name)
			self.db_set('status', 'Matured')
		
		if self.matured == 1 and self.renewed == 1:
			frappe.throw("FD is Not Update renewed and Matured  at a same time")
		if self.renewed == 1:
			if self.new_maturity_date <= self.matured_date:
				frappe.throw("Matured Date Can Not be less then Or equal FD Start Date")
			fd = frappe.new_doc("Fixed Deposit")
			fd.fd_number = self.fd_number
			fd.company = self.company
			fd.bank_account = self.bank_account
			fd.fd_account = self.fd_account
			fd.interest_account = self.interest_account
			fd.fd_start_date = utils.today()
			fd.fd_amount = self.renewal_amount
			fd.maturity_amount = self.new_maturity_amount
			fd.matured_date = self.new_maturity_date
			fd.previous_fd = self.name
			try:
				fd.save()
				fd.submit()
			except Exception as e:
				frappe.throw(str(e))
			else:
				url = get_url_to_form("Fixed Deposit",fd.name)
				frappe.msgprint("Fixed Deposit - <a href='{url}'>{doc}</a> is created".format(url=url, doc=frappe.bold(fd.name)))
			self.db_set('status', 'Renewed')
