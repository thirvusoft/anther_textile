import frappe
import frappe
import json
from frappe.model.naming import parse_naming_series
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter
import base64

from pyqrcode import create as qr_create
@frappe.whitelist()
def item_price(doc):
    doc = frappe.get_doc('Purchase Receipt',doc)
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
        
        
def get_serialno_barcode(doc):
    # for serialno in doc.items:
    stream = BytesIO()
    Code128(str(doc), writer=ImageWriter()).write(
        stream,
        {
            "module_width": 0.4,
            "text_distance": 1,
            "font_size": 20,
        },
    )
    barcode_base64 = base64.b64encode(stream.getbuffer()).decode()
    stream.close()

    return barcode_base64