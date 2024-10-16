from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')

	# Customizing the admin interface
	fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
	add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),  # Adding custom classes for styling
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    
	filter_horizontal = ()
	list_filter = ()
	ordering = ('email',)
    
	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.set_password(form.cleaned_data['password'])
		obj.save()

admin.site.register(Account, AccountAdmin)

# filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()
