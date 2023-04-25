frappe.listview_settings['FD Management'] = {

	add_fields: ['status'],
	get_indicator: function(doc) {
		
		if(doc.status === "Running"){
            return [__("Running"), "orange", "status,=,Running"];
        }
		if(doc.status === "Matured"){
            return [__("Matured"), "green", "status,=,Matured"];
        }
		if(doc.status === "Renewal"){
            return [__("Renewal"), "blue", "status,=,Renewal"];
        }
	},
	hide_name_column: true
};
