from django import forms
from .models import Recipie


class RecipieForm(forms.ModelForm):
	class Meta:
		model = Recipie
		fields = ('title','chef','recipie_details')


		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'chef': forms.Select(attrs={'class': 'form-control'}),
            'recipie_details': forms.Textarea(attrs={'class': 'form-control'}),
         }




		