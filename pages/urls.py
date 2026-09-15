from django.urls import path

from pages.views import home_page, about_page, contact_page, page_number, page_name, page_uuid


urlpatterns = [
    path('home/', home_page, name='home'), # type: ignore
    path('about/', about_page, name='about'), # type: ignore
    path('contact/', contact_page, name='contact'), # type: ignore
    path('by-number/<int:number>', page_number, name='page-number'), # type: ignore
    path('by-name/<str:name>', page_name, name='page-name'), # type: ignore
    path('by-uuid/<uuid:page_id>', page_uuid, name='page-page_id'), # type: ignore
]
