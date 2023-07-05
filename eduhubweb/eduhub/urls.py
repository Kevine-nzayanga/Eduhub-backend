from django.urls import path
from .views import showBooks

urlpatterns = [
    path('books/',showBooks,name= 'displaybooks'),
    path('books/<int:book_id>/', showBooks, name='book_detail_view'),
    path('books/<int:book_id>/delete/', showBooks, name='delete_book_view'),
]




