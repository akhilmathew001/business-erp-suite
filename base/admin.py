from django.contrib import admin

# Register your models here.

from base.models.company import Company, State, Country
from base.models.customer import Customer

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(State)
admin.site.register(Country)
