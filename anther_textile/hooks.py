from . import __version__ as app_version

app_name = "anther_textile"
app_title = "Anther Textile"
app_publisher = "Thrivusoft Private Limited"
app_description = "Anther Barcode Textile"
app_email = "thirvusoft@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/anther_textile/css/anther_textile.css"
# app_include_js = "/assets/anther_textile/js/anther_textile.js"

# include js, css files in header of web template
# web_include_css = "/assets/anther_textile/css/anther_textile.css"
# web_include_js = "/assets/anther_textile/js/anther_textile.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "anther_textile/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Purchase Receipt" : "anther_textile/utils/purchase_receipt.js",
              "Purchase Invoice" : "anther_textile/utils/purchase_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	"methods": "anther_textile.anther_textile.utils.purchase_receipt.get_serialno_barcode",
#	"filters": "anther_textile.utils.jinja_filters"
}

# Installation
# ------------

# before_install = "anther_textile.install.before_install"
# after_install = "anther_textile.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "anther_textile.uninstall.before_uninstall"
# after_uninstall = "anther_textile.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "anther_textile.utils.before_app_install"
# after_app_install = "anther_textile.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "anther_textile.utils.before_app_uninstall"
# after_app_uninstall = "anther_textile.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "anther_textile.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "Purchase Receipt" : {
	# 	"on_submit": "anther_textile.anther_textile.utils.purchase_receipt.item_price"
	# },
    # "Purchase Invoice" : {
	# 	"on_submit": "anther_textile.anther_textile.utils.purchase_invoice.item_price"
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"anther_textile.tasks.all"
#	],
#	"daily": [
#		"anther_textile.tasks.daily"
#	],
#	"hourly": [
#		"anther_textile.tasks.hourly"
#	],
#	"weekly": [
#		"anther_textile.tasks.weekly"
#	],
#	"monthly": [
#		"anther_textile.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "anther_textile.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "anther_textile.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "anther_textile.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["anther_textile.utils.before_request"]
# after_request = ["anther_textile.utils.after_request"]

# Job Events
# ----------
# before_job = ["anther_textile.utils.before_job"]
# after_job = ["anther_textile.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"anther_textile.auth.validate"
# ]
