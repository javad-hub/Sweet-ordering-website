from django.urls import path
from .views import HomePageView, TastePageView
from . import views

urlpatterns = [
	#path('', HomePageView.as_view(), name="home"),
	path('', views.HomePageView, name="home"),
	path('tastes/', TastePageView.as_view(), name="taste"),

]