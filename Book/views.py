from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.

from Book.models import Book, Author, AuthorDetail, Publish
import json


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'index.html')


def books(request):
    """

    :param request:
    :return:
    """
    book_list = Book.objects.all()

    return render(request, 'book.html', {'book_list': book_list})


def add_book(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        publish_list = Publish.objects.all()
        authors = Author.objects.all()
        return render(request, 'add_book.html', {'publish_list': publish_list, 'authors': authors})
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        authors = request.POST.get('authors')
        book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        book.authors.add(*authors)

        return redirect(reverse('books'))


def delete_book(request, del_book_id):
    """

    :param del_book_id:
    :param request:
    :param delete_book_id:
    :return:
    """
    Book.objects.filter(nid=del_book_id).delete()
    return redirect(reverse('books'))


def edit_book(request, edit_book_id):
    book_list = Book.objects.filter(nid=edit_book_id).first()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request, 'edit_book.html',
                  {'book_list': book_list, 'publish_list': publish_list, 'author_list': author_list})


def book_ajax_del(request, del_book_id):
    response = {"state": True}
    try:
        Book.objects.filter(pk=del_book_id).delete()
    except Exception as e:
        response = {"state": False}

    return HttpResponse(json.dumps(response))


