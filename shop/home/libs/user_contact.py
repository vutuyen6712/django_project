from django import forms
from home.models import user_contacts
class  UserContactFrom(forms.ModelForm):
	class Meta:
		model = user_contacts
		fields = "__all__" 