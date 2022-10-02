from django.contrib import admin
from good.models import Contact
from good.models import Register
from good.models import categ
from good.models import products


# Register your models here.

admin.site.register(Contact)
admin.site.register(Register) 
admin.site.register(products)
admin.site.register(categ)
