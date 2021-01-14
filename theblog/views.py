from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipie
from .forms import RecipieForm
from django.urls import reverse_lazy
from django.template.response import TemplateResponse

class HomeView(ListView):
	model = Recipie
	template_name= 'theblog/home.html'
	ordering = ['-id']
	#ordering = ['-publish_date']


class RecipieDetailView(DetailView):
	model = Recipie
	template_name = 'theblog/recipie_details.html'


class AddRecipieView(CreateView):
	model = Recipie
	form_class = RecipieForm
	template_name = 'theblog/add_recipie.html'

class UpdateRecipieView(UpdateView):
    model = Recipie
    form_class = RecipieForm
    template_name = 'theblog/update_recipie.html'

class DeleteRecipieView(DeleteView):
    model = Recipie
    template_name = 'theblog/delete_recipie.html'
    success_url = reverse_lazy('theblog:delete-success')


def DeleteSuccess(request):
	 return TemplateResponse(request,'theblog/delete_success.html')




