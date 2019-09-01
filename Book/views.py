"""
@Description: 
@Author: ggy
@Date: 2019-07-30 10:45:14
@LastEditTime: 2019-09-01 20:23:17
@LastEditors: ggy
"""
from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.

from Book.models import Book, Author, AuthorDetail, Publish
import json


def index(request):
    """
    首页页面
    :param request:
    :return:
    """
    return render(request, 'index.html')


def books(request):
    """
    书籍展示页面
    :param request:
    :return:
    """
    book_list = Book.objects.all()

    return render(request, 'book/book.html', {'book_list': book_list})


def add_edit_book(request, book_id=None):
    """
    添加编辑整合页面
    :param request:
    :param book_id:默认为空，有值传值
    :return:
    """

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    content = {
        'publish_list': publish_list,
        'author_list': author_list,
        'item': "添加书籍"
    }
    book_list = Book.objects.filter(nid=book_id).first()

    if request.method == "GET":

        if request.path != reverse('add_book'):
            content['book_list'] = book_list
            content['item'] = '编辑书籍'

        return render(request, 'book/add_edit_book.html', content)
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        authors = request.POST.getlist('authors')

        if request.path == reverse('add_book'):
            book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
            book.authors.add(*authors)

        else:
            Book.objects.filter(nid=book_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
            book_list.authors.set(authors)

        return redirect(reverse('books'))


# def delete_book(request, del_book_id):
#     """
#     删除书籍
#     :param del_book_id:
#     :param request:
#     :param delete_book_id:
#     :return:
#     """
#     Book.objects.filter(nid=del_book_id).delete()
#     return redirect(reverse('books'))


def book_ajax_del(request, del_book_id):
    """
    删除书籍得ajax
    :param request:
    :param del_book_id:
    :return:
    """

    response = {"state": True}

    try:

        Book.objects.filter(pk=del_book_id).delete()

    except Exception as e:

        response = {"state": False}

    return HttpResponse(json.dumps(response))


def publish(request):
    """
    出版社信息
    :param request:
    :return:
    """
    publish_list = Publish.objects.all()
    content = {
        'publish_list': publish_list,
    }
    return render(request, 'publish/publish.html', content)


def add_edit_publish(request, publish_id=None):
    """
    编辑修改出版社
    :param request:
    :param publish_id:
    :return:
    """
    publish_list = Publish.objects.filter(pk=publish_id).first()
    item = '添加出版社'
    if request.method == 'GET':

        if request.path == reverse('add_publish'):

            return render(request, 'publish/add_edit_publish.html', {'item': item})

        else:

            item = '修改出版社'
            return render(request, 'publish/add_edit_publish.html', {'publish_list': publish_list, 'item': item})

    else:
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')

            if request.path == reverse('add_publish'):
                Publish.objects.create(name=name, email=email)
            else:
                Publish.objects.filter(nid=publish_id).update(name=name, email=email)

            return redirect(reverse('publish'))

        except Exception as e:
            return HttpResponse('404!')
    #
    # if request.path == reverse('add_publish'):
    #
    #     if request.method == 'GET':
    #         return render(request, 'publish/add_publish.html')
    #
    #     else:
    #         try:
    #             name = request.POST.get('name')
    #             email = request.POST.get('email')
    #             Publish.objects.create(name=name, email=email)
    #
    #             return redirect(reverse('publish'))
    #
    #         except Exception as e:
    #             return HttpResponse('404!')
    #
    # else:
    #     if request.method == 'GET':
    #         return render(request)
    #     else:
    #         request.POST.get('name')
    #         request.POST.get('email')
    #         Publish.objects.filter(nid=publish_id).update(name=name, email=email)
    #         return redirect(reverse('publish'))


def delete_publish(request, publish_id):
    """
    删除出版社
    :param request:
    :param author_id:
    :return:
    """

    response = {"state": True}

    try:

        Publish.objects.filter(nid=publish_id).delete()

    except Exception as e:

        response = {"state": False}

    return HttpResponse(json.dumps(response))


def author(request):
    """
    作者信息
    :param request:
    :return:
    """
    author_list = Author.objects.all()
    content = {
        'author_list': author_list,
    }
    return render(request, 'author/author.html', content)


def add_edit_author(request, author_id=None):
    item = '添加作者'
    if request.method == 'GET':

        if request.path == reverse('add_author'):

            return render(request, 'author/add_edit_author.html', {'item': item})

        else:

            item = '编辑作者'
            author_list = Author.objects.filter(nid=author_id).first()
            return render(request, 'author/add_edit_author.html', {'author_list': author_list, 'item': item})

    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        addr = request.POST.get('addr')
        tel = request.POST.get('tel')
        print(addr, tel)

        if request.path == reverse('add_author'):

            ad = AuthorDetail.objects.create(addr=addr, tel=tel)
            Author.objects.create(name=name, age=age, email=email, ad=ad)

        else:

            ad = AuthorDetail.objects.filter(author__nid=author_id).update(addr=addr, tel=tel)
            Author.objects.filter(nid=author_id).update(name=name, age=age, email=email, ad=ad)

        return redirect(reverse('author'))


def delete_author(request, author_id):
    """
    删除用户
    :param request:
    :param publish_id:
    :return:
    """

    response = {"state": True}

    try:

        Author.objects.filter(nid=author_id).delete()

    except Exception as e:

        response = {"state": False}

    return HttpResponse(json.dumps(response))
