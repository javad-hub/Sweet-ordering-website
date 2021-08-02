from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Sweet
from .forms import OrderForm
# Create your views here.

#class HomePageView(TemplateView):
#	form = OrderForm()
#	template_name = 'home.html'

def HomePageView(request):
	return render(request, "home.html", {
		"form":OrderForm()})

class TastePageView(ListView):
	model = Sweet
	template_name = "taste.html"