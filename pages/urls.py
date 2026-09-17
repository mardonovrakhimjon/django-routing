from django.urls import path

from pages.views import (
    home_page,
    about_page,
    contact_page,
    page_number,
    page_name,
    page_uuid,
    http_request_view,
    calculate_view,
    random_view,
)


urlpatterns = [
    path("home/<str:name>", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("contact/", contact_page, name="contact"),
    path("by-number/<int:number>", page_number, name="page-number"),
    path("by-name/<str:name>", page_name, name="page-name"),
    path("by-uuid/<uuid:page_id>", page_uuid, name="page-page_id"),
    path("http-request/<int:id>", http_request_view, name="https-request"),
    path("calculate/", calculate_view, name="calculate"),
    path("random/", random_view, name="calculate"),
]
