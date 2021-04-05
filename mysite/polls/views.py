from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# Create your views here.
from .models import Question

# index page : 최근 질문들 표시 -> model을 이용+render
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# detail : 질문 내용과 투표할 수 있는 서식 표시 -> model 이용+render+404 error
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# result : 특정 질문에 대한 결과 표시
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# vote : 특정 질문에 대해 특정 선택할 수 있는 투표 기능 표시
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)