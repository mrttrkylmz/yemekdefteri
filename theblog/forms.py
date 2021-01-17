from django import forms
from .models import Recipie, Comment


class RecipieForm(forms.ModelForm):
	class Meta:
		model = Recipie
		fields = ('title','chef','recipie_details','header_image')


		widgets = {
                  'title': forms.TextInput(attrs={'class': 'form-control'}),
                  'chef': forms.TextInput(attrs={'class': 'form-control' , 'value':'', 'id':'elder', 'type' : 'hidden'}),
                  #'chef': forms.Select(attrs={'class': 'form-control'}),
                  'recipie_details': forms.Textarea(attrs={'class': 'form-control'}),
         }


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)
		ordering = ['-id']


		widgets = {
                  #'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'body': forms.Textarea(attrs={'class': 'form-control'}),
         }




		