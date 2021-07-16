from django.urls import path
from .views import HomePageView, TastePageView

urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('tastes/', TastePageView.as_view(), name="taste"),

]