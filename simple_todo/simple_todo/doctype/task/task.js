frappe.listview_settings['Task'] = {
    add_fields: ["is_completed"],
    get_indicator: function(doc) {
        if (doc.is_completed) {
            return [__("Completed"), "green", "is_completed,=,1"];
        } else {
            return [__("Pending"), "orange", "is_completed,=,0"];
        }
    },
    onload: function(listview) {
        listview.page.add_menu_item(__("Hide Completed Tasks"), function() {
            listview.filter_area.add([[listview.doctype, "is_completed", "=", 0]]);
        });
        
        listview.page.add_menu_item(__("Show All Tasks"), function() {
            listview.filter_area.clear();
        });
    }
};