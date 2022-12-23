from django.contrib import admin
from .models import Arena, Artist, Show, Ticket, Visitor

admin.site.register(Arena)
admin.site.register(Artist)
admin.site.register(Show)
admin.site.register(Ticket)
admin.site.register(Visitor)