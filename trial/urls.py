from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_trial, name='all_trial'),
    path('<int:trial_id>/', views.trial_detail, name='trial_detail'),
    path('trial_stores/', views.trial_store_view, name='trial_store')
]
