from django.contrib import admin
from website.models import Customer, Service, FAQ, Message
# Register your models here.

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(FAQ)
admin.site.register(Message)