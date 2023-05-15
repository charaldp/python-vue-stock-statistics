from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('stock_ratings/', views.stock_ratings),
    path('stock_ratings/<int:pk>/', views.stock_rating_detail),
]