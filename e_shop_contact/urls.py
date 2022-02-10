from django.urls import path

from .views import contact_page, contact_us_done

urlpatterns = [
    path('contact_us', contact_page, name='contact_us'),
    path('contact_us_done', contact_us_done),


]
