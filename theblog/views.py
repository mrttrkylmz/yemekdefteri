from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipie


class HomeView(ListView):
	model = Recipie
	template_name= 'theblog/home.html'


class RecipieDetailView(DetailView):
	model = Recipie
	template_name = 'theblog/recipie_details.html'