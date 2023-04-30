from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('narimanov', narimanov_view, name='narimanov'),
    path('binagadi', binagadi_view, name='binagadi'),
    path('nasimi', nasimi_view, name='nasimi'),
    path('khatai', khatai_view, name='khatai'),
    path('yasamal', yasamal_view, name='yasamal'),
    path('surakhani', surakhani_view, name='surakhani'),
    path('sabayil', sabayil_view, name='sabayil'),
    path('nizami', nizami_view, name='nizami'),
    path('namelum', namelum_view, name='namelum'),
]


