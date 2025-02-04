from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('contact_success_view/', views.contact_success_view, name='contact_success_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]