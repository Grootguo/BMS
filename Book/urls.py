from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/add_book/', views.add_book, name='add_book'),
    re_path('books/delete/(?P<del_book_id>\d+)', views.delete_book, name='del_book'),
    re_path('books/edit/(?P<edit_book_id>\d+)', views.edit_book, name='edit_book'),
    re_path("^books/ajax_delete/(?P<del_book_id>\d+)/$", views.book_ajax_del),
]
