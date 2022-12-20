from django.contrib import admin
from .models import Poems, Message

# Register your models here.
admin.site.register(Poems)
admin.site.register(Message)