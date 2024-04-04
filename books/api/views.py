from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from ..models import Book  # Adjust the path according to your project structure

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/books/',
        '/api/books/<id>/',
        # Add other routes if necessary
    ]
    return Response(routes)

@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
