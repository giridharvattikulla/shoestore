from django.urls import path
from . import views

urlpatterns = [
    path('', views.ex, name='ex'),
    path('pone/', views.pone, name='pone'),
    path('ptwo/', views.ptwo, name='ptwo'),
    path('pthree/', views.pthree, name='pthree'),
    path('pfour/', views.pfour, name='pfour'),
    path('reviews/', views.review_page, name='review'),
]
