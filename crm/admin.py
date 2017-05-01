from django.contrib import admin
from crm.models.lead import CrmLead
from crm.models.product import Product,ProductUOM

# Register your models here.

admin.site.register(CrmLead)
admin.site.register(ProductUOM)
admin.site.register(Product)