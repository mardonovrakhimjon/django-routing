from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')


def page_number(request: HttpRequest, number: int) -> HttpResponse:
    return render(request, 'number.html', {'number': number})


def page_name(request: HttpRequest, name: str) -> HttpResponse:
    return render(request, 'name.html', {'name': name})


def page_uuid(request: HttpRequest, page_id: str) -> HttpResponse:
    return render(request, 'uuid.html', {'page_id': page_id})
