from django.http import HttpResponse

from polls.models import Question


def index(request):
    latest_question_list =  Question.objects.order_by("-pub_date")[:5]
    return HttpResponse(", ".join([q.question_text for q in latest_question_list]))

def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You are looking at results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
