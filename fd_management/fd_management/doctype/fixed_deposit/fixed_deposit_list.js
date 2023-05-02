frappe.listview_settings['Fixed Deposit'] = {

	add_fields: ['status'],
	get_indicator: function(doc) {
		
		if(doc.status === "Running"){
            return [__("Running"), "orange", "status,=,Running"];
        }
		if(doc.status === "Matured"){
            return [__("Matured"), "red", "status,=,Matured"];
        }
		if(doc.status === "Renewed"){
            return [__("Renewed"), "blue", "status,=,Renewed"];
        }
		if(doc.status === "Padding"){
            return [__("Padding"), "green", "status,=,Padding"];
        }
	},
	hide_name_column: true
};
