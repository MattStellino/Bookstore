from rest_framework import serializers
from ..models import Book  # Adjust the path according to your project structure

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'rating', 'description']
