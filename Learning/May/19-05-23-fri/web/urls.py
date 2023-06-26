from django.urls import path
#from .views import home_page, about_page, contact_page
from .views import HomePage, AboutPage, ContactPage

urlpatterns = [
    # path("", home_page, name='home'),
    # path("about/", about_page, name='about'),
    # path("contact/", contact_page, name='contact'),



    path("", HomePage.as_view(), name='home'),
    path("about/", AboutPage.as_view(), name='about'),
    path("contact/", ContactPage.as_view(), name='contact'),

]
