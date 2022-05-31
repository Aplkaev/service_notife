from django.contrib import admin

# Register your models here.
from .models import Mailing, Message, Client

admin.site.register(Mailing)
admin.site.register(Message)
admin.site.register(Client)