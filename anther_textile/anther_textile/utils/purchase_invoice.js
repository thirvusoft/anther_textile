frappe.ui.form.on('Purchase Invoice', {
    on_submit: function(frm){
      frm.doc.items.forEach(row => {
        var item_price = frappe.model.get_new_doc('Item Price')
        item_price.item_code = row.item_code
        item_price.price_list = "Standard Selling" 
        item_price.batch_no = row.batch_no || ""
        item_price.price_list_rate = row.custom_mrp 
        item_price.valid_from = frm.doc.posting_date   
        frappe.call({method:"frappe.client.save", args:{doc:item_price}})
      })
     }
  })