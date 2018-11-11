from django.contrib import admin
from .models import *

class SubscriberAdmin (admin.ModelAdmin):
    #list_display = [field.name for field in]
    list_display = ["name","email"]
    list_filter = ["name","email"]
    search_fields = ["name", "email"]
    exclude = ["email"]

    class Meta:
        model = Subscriber
admin.site.register(Subscriber, SubscriberAdmin)