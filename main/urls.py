from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('',views.homePage, name='home'),
	path('about/',views.aboutPage, name='about'),
	path('contact/',views.contactPage, name='contact'),
]