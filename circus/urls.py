from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('arena', views.arena, name='arena'),
    path('ticket', views.ticket, name='ticket'),
    path('visitor', views.visitor, name='visitor'),
    path('show', views.show, name='show'),
    path('artist', views.artist, name='artist'),

    path('arena_delete_all', views.arena_delete_all, name='arena_delete_all'),
    path('arena_delete/<int:id>', views.arena_delete, name='arena_delete'),
    path('arena_update', views.arena_update, name='arena_update'),
]