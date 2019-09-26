from django import forms
from home.models import user
class  UserForm(forms.ModelForm):
	class Meta:
		model = user
		fields = "__all__"
 