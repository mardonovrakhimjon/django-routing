from random import randint
import secrets
import string

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from easy_password_generator import PassGen


def home_page(request: HttpRequest, name: str) -> HttpResponse:
    return render(request=request, template_name="home.html", context={"name": name})


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


def page_number(request: HttpRequest, number: int) -> HttpResponse:
    return render(request, "number.html", {"number": number})


def page_name(request: HttpRequest, name: str) -> HttpResponse:
    return render(request, "name.html", {"name": name})


def page_uuid(request: HttpRequest, page_id: str) -> HttpResponse:
    return render(request, "uuid.html", {"page_id": page_id})


def http_request_view(request: HttpRequest, id: int) -> HttpResponse:
    params = request.GET

    min_price = params.get("min-price")
    max_price = params.get("max-price")

    print(min_price, max_price)

    return HttpResponse()


def calculate_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        params = request.GET

        a = params.get("a")
        b = params.get("b")

        result = int(a) + int(b)

        return JsonResponse({"result": result})
    return HttpResponse("Page not found")


def random_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request=request, template_name="random.html")
    elif request.method == "POST":
        data = request.POST

        type = data.get("type")
        if type == "number":
            a = int(data.get("a"))
            b = int(data.get("b"))

            random_number = randint(a, b)

            return render(
                request=request,
                template_name="random.html",
                context={"result": random_number, "a": a, "b": b},
            )

        elif type == "password":
            length = int(data.get("length"))

            password = "".join(
                secrets.choice(string.ascii_letters + string.digits)
                for _ in range(length)
            )

            return render(
                request=request,
                template_name="random.html",
                context={"result": password},
            )
