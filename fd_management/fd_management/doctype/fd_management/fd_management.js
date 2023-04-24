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
	}
});
