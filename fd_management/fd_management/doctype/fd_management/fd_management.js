// Copyright (c) 2023, finbyx and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fd Management', {
	refresh: function(frm) {
		frm.set_query('interest_account', function(doc) {
				return {
					filters: {
						"is_group": 0,
					
					}
				};
			});
		frm.set_query('fd_account', function(doc) {
			return {
				filters: {
					"is_group": 0,
				
				}
			};
		});
		frm.set_query('bank_account', function(doc) {
			return {
				filters: {
					"is_group": 0,
				
				}
			};
		});
	},
	matured_amount:function(frm){
		if(!frm.doc.matured_amount__1){
			frm.set_value('matured_amount__1',frm.doc.matured_amount);
		}
	},
	matured_amount__1:function(frm){
		if(frm.doc.matured_amount__1 < frm.doc.fd_amount){
			frappe.throw("Matured Amount Can Not be less then  FD Amount")
		}
		frm.set_value('interest_amount',(frm.doc.matured_amount__1 - frm.doc.fd_amount));
	}
});
