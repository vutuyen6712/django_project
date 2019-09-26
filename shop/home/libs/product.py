from django import forms
from home.models import Product
class  ProductFrom(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__" 