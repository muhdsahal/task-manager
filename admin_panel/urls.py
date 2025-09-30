from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('superadmin/dashboard/', views.superadmin_dashboard, name='superadmin-dashboard'),
    path('no-permission/', views.no_permission, name='no-permission')

]
