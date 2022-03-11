from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Partha Ice Cream Admin"
admin.site.site_title = "Partha Ice Cream"
admin.site.index_title = "Welcome to Partha Ice Cream"
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
]
