from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # 图书管理
    path('books/', views.books, name='books'),
    path('books/add_book/', views.add_edit_book, name='add_book'),
    re_path('books/edit/(?P<book_id>\d+)', views.add_edit_book, name='edit_book'),
    re_path("^books/ajax_delete/(?P<del_book_id>\d+)/$", views.book_ajax_del),

    # re_path('books/delete/(?P<del_book_id>\d+)', views.delete_book, name='del_book'),
    
    # 出版社管理
    path('publish/', views.publish, name='publish'),
    path('publish/add_publish/', views.add_edit_publish, name='add_publish'),
    re_path('publish/edit_publish/(?P<publish_id>\d+)', views.add_edit_publish, name='edit_publish'),
    re_path('publish/del_publish/(?P<publish_id>\d+)/', views.delete_publish, name='del_publish'),

    # 作者管理
    path('author/', views.author, name='author'),
    path('author/add_author/', views.add_edit_author, name='add_author'),
    re_path('author/edit_author/(?P<author_id>\d+)', views.add_edit_author, name='edit_author'),
    re_path('author/del_author/(?P<author_id>\d+)/', views.delete_author, name='del_author'),
]
