from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Recipies,Comments
from django.template import loader
from django.http import Http404

# Create your views here.


def index(request):
    latest_recipies_list = Recipies.objects.order_by('-pub_date')[:5]
    template = loader.get_template('recipies/index.html')
    context = {
        'latest_recipies_list': latest_recipies_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, recipies_id):
    recipies = get_object_or_404(Recipies, pk=recipies_id)
    return render(request, 'recipies/detail.html', {'recipies':recipies})

def results(request, recipies_id):
    response = "oylar %s."
    return HttpResponse(response % recipies_id)

def upvote(request, recipies_id):
    return HttpResponse("upvote %s." % question_id)

def downvote(request, recipies_id):
    return HttpResponse("downvote %s." % question_id)

