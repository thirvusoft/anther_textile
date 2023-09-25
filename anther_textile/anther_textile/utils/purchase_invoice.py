import frappe

@frappe.whitelist()
def item_price(doc):
    doc = frappe.get_doc('Purchase Invoice',doc)
    for item in doc.items:
        item_price_list=frappe.new_doc("Item Price")
        item_price_list.item_code = item.item_code
        item_price_list.price_list = "Standard Buying"
        item_price_list.batch_no = item.batch_no
        item_price_list.price_list_rate = item.custom_mrp
        item_price_list.valid_from = doc.posting_date
        try:
            item_price_list.save()
            frappe.db.commit()
            frappe.msgprint("Item Price Created")
        except Exception as e:
            frappe.throw(f"Batch-{item_price_list.batch_no} Already have this MRP - {item_price_list.price_list_rate } ")
        