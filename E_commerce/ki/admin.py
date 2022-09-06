from django.contrib import admin
from ki.models import MyUser, Product, Category, Order, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class MyUserAdmin(BaseUserAdmin):
	list_display = ('email', 'Date_joined', 'is_admin', 'is_active')
	search_fields = ('email',)
	readonly_fields = ('Date_joined',)
	filter_horizontal = ()
	list_filter = ('Date_joined',)
	fieldsets = ()

	add_fieldsets = (
		(None, {
			'classes': ('wide'),
			'fields': ('email', 'password1', 'password2'),
		}),
	)

	ordering = ('email',)
admin.site.register(MyUser)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
