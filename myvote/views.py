from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list} # 담아가기
    return render(request, 'display.html', context)

def DetailFunc(request, question_id):   # urls에서 question_id를 더 받아옴
    #return HttpResponse('You are voting on question %s'%question_id) # 타고 넘어왔는지 보기위해
    #return HttpResponse('You are voting on question {}'.format(question_id)) # 타고 넘어왔는지 보기위해
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        print('Question 자료 에러')
        raise Http404("Question DoesNotExist")
    '''
    
    question = get_object_or_404(Question, pk=question_id) #위에 try except를 안쓰고 이렇게 쓸 수 있음
    #print(question.question_text)
    #print(question)
    #print(question.pub_date)
    return render(request, 'detail.html', {'question':question})

def VoteFunc(request, question_id):   #question_id넘어옴
    #return HttpResponse('voting on question_id %s'%question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choice_set.get(pk = request.POST.get('choice')) #detail.html name값이 넘어옴
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'err_msg':'1개의 항목을 선택하세요'})
    
    sel_choice.votes += 1 # 투표가 완료된 선택 항목에 대해 1씩 누적
    sel_choice.save()  # votes가 갱신
    print(reverse('results', args=(question_id,)))
    return HttpResponseRedirect(reverse('results', args=(question_id,)))

def ResultFunc(request, question_id):
    #return HttpResponse('result of question_id : %s'%question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question':question})