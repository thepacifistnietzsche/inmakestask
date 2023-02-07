from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    #path('profile/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='persons/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='persons/logout.html'), name="logout"),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]