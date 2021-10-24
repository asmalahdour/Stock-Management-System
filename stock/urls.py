from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('home/', views.home, name='home'),

    path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
    path('fprofile/', views.fprofile, name='fprofile'),
    path('view_profile/', views.view_profile, name='view_profile'),

    path('', views.list_item, name='list_item'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),


]
