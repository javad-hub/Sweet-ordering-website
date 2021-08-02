from django import forms

tastes = (
	("lemon", "Lemon"),
	("strawberry", "Strawberry"),
	)
class OrderForm(forms.Form):
	name = forms.CharField(max_length=200)
	phone = forms.IntegerField()
	address = forms.Textarea()
	taste = forms.ChoiceField(choices = tastes)
