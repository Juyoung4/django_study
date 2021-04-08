from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Board, Category
from .forms import BoardForm
from django.contrib.auth.models import User

# Create your views here.
def board_post(request):
    if not request.session.get('user'): # sessions끊겼는지 확인
        return redirect('/accounts/')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            print("pass!!!!")
            new_board = form.save(commit=False)
            new_board.writer = request.user
            new_board.save()
            return redirect('/board/')
        else:
            return HttpResponse(form.errors.values())
    else:
        categorynames = Category.objects.all()
        return render(request, 'board/board_new.html', {'Category': categorynames})

def board_list(request):
    if not request.session.get('user'):  # sessions끊겼는지 확인
        return redirect('/accounts/')

    user = request.user
    myBoard = Board.objects.filter(writer=user).order_by('-created_at') # 내 게시글만 가져와야 되니께
    return render(request, 'board/my_board.html', {'myBoard' : myBoard})
