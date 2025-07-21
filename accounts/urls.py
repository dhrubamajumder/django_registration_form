from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dash_view, name='dash'),
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dash/', views.dash_view, name='dash' ),
    path('info/', views.info_view, name='info'),

    path('delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('update/<int:pk>/', views.update_user, name='update_user'),

]
