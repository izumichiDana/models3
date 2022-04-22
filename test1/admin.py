from django.contrib import admin

from test1.models import Admin, Order

admin.site.register(Order)
admin.site.register(Admin)

