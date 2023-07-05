from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def showBooks(request, book_id=None):
    if request.method == 'GET':
        if book_id is not None:
            book = Book.objects.filter(id=book_id).first()
            if book is not None:
                serializer = BookSerializer(book)
                return Response(serializer.data)
            return Response({'error': 'Book not found'}, status=404)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        book = Book.objects.filter(id=book_id).first()
        if book is not None:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({'error': 'Book not found'}, status=404)
    elif request.method == 'DELETE':
        book = Book.objects.filter(id=book_id).first()
        if book is not None:
            book.delete()
            return Response(status=204)
        return Response({'error': 'Book not found'}, status=404)
    return Response(status=400)