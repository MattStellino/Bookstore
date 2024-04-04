from django.urls import path
from .api import views as api_views

urlpatterns = [
    path('api/books/', api_views.getBooks, name='api-books'),
    path('api/books/<int:pk>/', api_views.getBook, name='api-book'),
    path('api/', api_views.getRoutes, name='api-routes'),
]
