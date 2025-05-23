# Url Dispatching
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Sushant Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Sushant Database"

urlpatterns = [
    # defining path 
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name="contact"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
]