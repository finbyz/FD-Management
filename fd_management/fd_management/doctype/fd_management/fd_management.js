// Copyright (c) 2023, finbyx and contributors
// For license information, please see license.txt

frappe.ui.form.on('FD Management', {
	refresh: function(frm) {
		frm.set_query('interest_account', function(doc) {
				return {
					filters: {
						"is_group": 0,
						'company':frm.doc.company
					}
				};
			});
		frm.set_query('fd_account', function(doc) {
			return {
				filters: {
					"is_group": 0,
					'company':frm.doc.company
				}
			};
		});
		frm.set_query('bank_account', function(doc) {
			return {
				filters: {
					"is_group": 0,
					'company':frm.doc.company
				}
			};
		});
		if(frm.doc.status == 'Renewal'){
			frm.set_df_property('matured', 'hidden', 1)
		}
		if(frm.doc.status == 'Matured'){
			frm.set_df_property('renewal', 'hidden', 1)
		}
	},
	
	matured:function(frm){
		if(frm.doc.matured==1){
			if(frm.doc.maturity_amount){
				frm.set_value('matured_amount',frm.doc.maturity_amount);
				frm.set_value('interest_amount',(frm.doc.matured_amount - frm.doc.fd_amount));
			}
			if(frm.doc.renewal==1)
				frm.set_value('renewal',0);
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
			if(frm.doc.matured==1)
				frm.set_value('matured',0);
		}
	},
	renewal_amount:function(frm)
	{
		frm.set_value('renewal_interest_amount',(frm.doc.renewal_amount - frm.doc.fd_amount));
	},


});	
