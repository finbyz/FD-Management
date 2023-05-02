from . import __version__ as app_version

app_name = "fd_management"
app_title = "Fd Management"
app_publisher = "finbyx"
app_description = "fd management"
app_email = "info@finbyz.tech"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fd_management/css/fd_management.css"
# app_include_js = "/assets/fd_management/js/fd_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/fd_management/css/fd_management.css"
# web_include_js = "/assets/fd_management/js/fd_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fd_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_list_js = {"Fixed Deposit" : "fd_management/fd_management/doctype/fixed_deposit/fixed_deposit_list.js"}
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
# jinja = {
#	"methods": "fd_management.utils.jinja_methods",
#	"filters": "fd_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "fd_management.install.before_install"
# after_install = "fd_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "fd_management.uninstall.before_uninstall"
# after_uninstall = "fd_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fd_management.notifications.get_notification_config"

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

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
        "Journal Entry":
        {
            "on_cancel": "fd_management.fd_management.doctype.journal_entry.on_cancel"
        },
    }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"fd_management.tasks.all"
#	],
#	"daily": [
#		"fd_management.tasks.daily"
#	],
#	"hourly": [
#		"fd_management.tasks.hourly"
#	],
#	"weekly": [
#		"fd_management.tasks.weekly"
#	],
#	"monthly": [
#		"fd_management.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "fd_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "fd_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "fd_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["fd_management.utils.before_request"]
# after_request = ["fd_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["fd_management.utils.before_job"]
# after_job = ["fd_management.utils.after_job"]

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
#	"fd_management.auth.validate"
# ]
