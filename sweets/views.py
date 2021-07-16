from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Sweet
# Create your views here.

class HomePageView(TemplateView):
	template_name = 'home.html'

class TastePageView(ListView):
	model = Sweet
	template_name = "taste.html"