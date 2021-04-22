from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('create', views.create, name="create"),
    path('create-uuid', views.create_uuid, name="create.uuid"),
    path('show/<int:num>', views.show, name="show"),
    path('delete/<int:num>', views.destroy, name="destroy"),
    path('edit/<int:num>', views.edit, name="edit")
]
