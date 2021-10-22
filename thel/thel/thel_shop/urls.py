from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('all/', Category.as_view(), name='all_category'),
    path('category/<int:category_id>/', Get_category.as_view(), name='category'),
    path('faq/', faq, name='faq'),
    path('thel_society/', thel_society, name='thel_society'),
    path('about_us/', about_us, name='about_us'),
    path('clothes/<int:pk>/', Clothe_detail.as_view(), name='clothe_detail'),
    
]
