from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipie
from .forms import RecipieForm
from django.urls import reverse_lazy, reverse
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
	recipie = get_object_or_404(Recipie, id=request.POST.get('recipie_id'))
	liked = False
	if recipie.likes.filter(id=request.user.id).exists():
		recipie.likes.remove(request.user)
		liked = False
	else:
		recipie.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('theblog:recipie-detail', args=[str(pk)]))



class HomeView(ListView):
	model = Recipie
	template_name= 'theblog/home.html'
	ordering = ['-id']
	#ordering = ['-publish_date']


class RecipieDetailView(DetailView):
	model = Recipie
	template_name = 'theblog/recipie_details.html'

	def get_context_data(self, *args, **kwargs):

		stuff = get_object_or_404(Recipie, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context = super(RecipieDetailView, self).get_context_data(*args, **kwargs)
		context["total_likes"] =total_likes
		context["liked"] = liked
		return context


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




