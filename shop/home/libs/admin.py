from django import forms
from home.models import admin
class  adminForm(forms.ModelForm):
	class Meta:
		model = admin
		fields = "__all__"
