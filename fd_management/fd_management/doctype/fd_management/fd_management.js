// Copyright (c) 2023, finbyx and contributors
// For license information, please see license.txt

frappe.ui.form.on('FD Management', {
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
	
	matured:function(frm){
		if(frm.doc.matured==1){
			if(frm.doc.maturity_amount){
				frm.set_value('matured_amount',frm.doc.maturity_amount);
				frm.set_value('interest_amount',(frm.doc.matured_amount - frm.doc.fd_amount));
			}
		}
	},
	matured_amount:function(frm)
	{
		frm.set_value('interest_amount',(frm.doc.matured_amount - frm.doc.fd_amount));
	},
	renewal:function(frm){
		if(frm.doc.renewal==1){
			if(frm.doc.maturity_amount){
				frm.set_value('renewal_amount',frm.doc.maturity_amount);
				frm.set_value('renewal_interest_amount',(frm.doc.renewal_amount - frm.doc.fd_amount));
			}
		}
	},
	renewal_amount:function(frm)
	{
		frm.set_value('renewal_interest_amount',(frm.doc.renewal_amount - frm.doc.fd_amount));
	},


});	
