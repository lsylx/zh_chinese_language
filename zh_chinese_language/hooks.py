from . import __version__ as app_version

app_name = "zh_chinese_language"
app_title = "ZH Chinese language"
app_publisher = "Phipsoft"
app_description = "ZH Chinese language"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "huzj@phipsoft.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zh_chinese_language/css/zh_chinese_language.css"
# app_include_js = "/assets/zh_chinese_language/js/zh_chinese_language.js"
app_include_js = [
    "/assets/js/zh.min.js"
]
# include js, css files in header of web template
# web_include_css = "/assets/zh_chinese_language/css/zh_chinese_language.css"
# web_include_js = "/assets/zh_chinese_language/js/zh_chinese_language.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "zh_chinese_language/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Installation
# ------------

# before_install = "zh_chinese_language.install.before_install"
# after_install = "zh_chinese_language.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "zh_chinese_language.uninstall.before_uninstall"
# after_uninstall = "zh_chinese_language.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zh_chinese_language.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zh_chinese_language.tasks.all"
# 	],
# 	"daily": [
# 		"zh_chinese_language.tasks.daily"
# 	],
# 	"hourly": [
# 		"zh_chinese_language.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zh_chinese_language.tasks.weekly"
# 	]
# 	"monthly": [
# 		"zh_chinese_language.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "zh_chinese_language.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zh_chinese_language.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "zh_chinese_language.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"zh_chinese_language.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
