from django.urls import path
from foodbyorder import views

urlpatterns = [
    path('', views.login_page, name='login'), 
    path('create/', views.create_data, name='createfood'),
    path('view/', views.read_data, name='viewfood'),
    path('update/<int:pk>/', views.update_data, name='updatefood'),
    path('delete/<int:pk>/', views.delete_data, name='deletefood'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/pdf/', views.generate_pdf, name='pizza_pdf'),
]
