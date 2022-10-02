from django.contrib import admin
from cart.models import cartlist
from cart.models import items

# Register your models here.

admin.site.register(cartlist)
admin.site.register(items)
