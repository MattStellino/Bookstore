from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='api-get-routes'),  
    path('books/', views.getBooks, name='get-books'),
    path('books/<int:pk>/', views.getBook, name='get-book'),
   
]
