from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from Book.models import Book,Author,AuthorDetail,Publish
from django.views import View
from django.http import JsonResponse

from json import dumps
from django.core import serializers

class index(View):

    def get(self, request):

        return render(request, 'index.html')



class Books(View):

    def get(self, request):
        book = Book.objects.all()
        publish = Publish.objects.all()
        authors = Author.objects.all()
        return render(request, 'book.html', {'book': book, 'publish': publish, 'authors': authors})

    def psot(self, request, respones):
        print(respones)

        return

    def delete(self):

        return render()

    def put(self):

        return render()


