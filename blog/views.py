from django.shortcuts import render
from .models import Question
def post_list(request):
    posts = Question.objects.order_by('query')
    return render(request, 'blog/post_list.html', {'posts':posts})
#Create your views here.
