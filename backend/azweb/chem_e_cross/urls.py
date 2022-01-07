from django.urls import path

from . import views

app_name = "chem_e_cross"



urlpatterns = [
    path('',views.user_register2,name='quiz'),


]
