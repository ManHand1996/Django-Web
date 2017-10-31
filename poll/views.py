from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect
# use generic view system
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Question,Choice
# Create your views here.
"""
through function to define view
"""
# def index(request):
# 	# latest order
# 	questions_list = Question.objects.order_by("-pub_date")[:5]
# 	#context are assign tmplate variable names to python objects
# 	context = {
# 		"latest_question_list":questions_list,
# 	}
# 	# render(request,tmpDir,context) return a HttpResponse object 
# 	return render(request,"poll/index.html",context)
# 	# return HttpResponse(tmp.render(context,request))

# def detail(request,question_id):
# 	# try:
# 	# 	question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exist")

# 	# common idiom to replace above a few of lines code
# 	# for loose coupling
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'poll/detail.html',{'question':question})

def results(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'poll/results.html',{'question':question})

def vote(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(reqeust,'poll/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice"
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# redirect a view page
		# reverse will return url string like
		# 'poll/3/results'
		# use namespace to find view
		return HttpResponseRedirect(reverse('poll:results',args=(question.id,)))

"""
use generic view system to define view

"""
class IndexView(generic.ListView):
	template_name = 'poll/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		print("use get_queryset")
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'poll/detail.html'

	def get_queryset(self):
		print("use get_queryset")
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'poll/results.html'