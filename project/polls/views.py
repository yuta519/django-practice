from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": latest_question_list }
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You are looking at results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
