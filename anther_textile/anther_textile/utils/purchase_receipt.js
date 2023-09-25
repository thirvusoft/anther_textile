frappe.ui.form.on('Purchase Receipt', {
    refresh: function (frm) {
      if (!frm.doc.__islocal) {
        let r = cur_frm.add_custom_button("Create Item Price", async function () {
          frappe.call({
            method: "anther_textile.anther_textile.utils.purchase_receipt.item_price",
            args:{'doc':frm.doc.name}
          })
        })
        r[0].style.backgroundColor ="green" 
        r[0].style.color = "white"
      }
  
    },
  })