from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, template, context)


def books_date(request, pub_date):
    template = 'books/books_filter.html'
    page_number = request.GET.get(pub_date)
    dat = Book.objects.all().values('pub_date').order_by('pub_date')
    paginator = Paginator(dat, 10)
    page = paginator.get_page(page_number)
    context = {
        'book_list': Book.objects.filter(pub_date=pub_date),
        'page': page,
    }
    return render(request, template, context)

