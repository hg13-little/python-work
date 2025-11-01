from users import Admin

admin = Admin("Laura", "Smith", 40, "Chicago", "laura@example.com")
admin.describe_user()
admin.privileges.show_privileges()