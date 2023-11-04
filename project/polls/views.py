from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You are looking at results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
