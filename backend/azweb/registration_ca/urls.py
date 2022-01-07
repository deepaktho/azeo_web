from django.urls import path

from . import views

app_name = "registration_ca"



urlpatterns = [
<<<<<<< HEAD
    path('',views.Registration,name='index'),
    path('register', views.user_register, name = "register"),

=======
    path('',views.Index, name = 'main_website'),
    path('competitions',views.Competition, name = 'competition'),
    path('events',views.Events, name = 'events'),
    path('about_us',views.About_us, name = 'about_us'),
    path('sponsors',views.Sponsors, name = 'sponsors'),
    path('workshop',views.Workshop, name = 'workshop'),
    path('ca',views.Registration,name='index'),
    path('register', views.user_register, name = "register"),
    path('azeo_id',views.AZeo_id, name='azeo_id'),
    path('competitions/chem-o-philia', views.Chem_o_philia, name ='chem-o-philia'),
    path('competitions/chem-e-cross', views.Chem_e_cross, name ='chem-e-cross'),
   
>>>>>>> 4f1cfd245cef821d03f983f4d04bacb319e9bd0d
]

