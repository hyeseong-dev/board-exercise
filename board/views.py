from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect

from django.db import connection

import pymysql

def home(request):
    return render(request, 'home.html')

def board(request):
    rsBoard = Board.objects.all()
    return render(request, 'board_list.html', {'rsBoard': rsBoard})

def board_write(request):
    return render(request, 'board_write.html')

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')
    else:
        return redirect('/board_write')
        
def board_view(request):
    bno = int(request.GET.get('b_no', 1))
    rsDetail = Board.objects.filter(b_no=bno)
    return render(request, 'board_view.html', {'rsDetail': rsDetail})
    
def board_edit(request):
    bno = request.GET.get('b_no')
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, 'board_edit.html', {
        'rsDetail': rsDetail
    })

def board_update(request):
    try:
        bno = int(request.GET.get('b_no'))
        btitle = request.GET.get('b_title')
        bnote = request.GET.get('b_note')
        bwriter = request.GET.get('b_writer')

        board = Board.objects.get(b_no=bno)
        
        if btitle is not None or bnote is not None or bwriter is not None:
            board.b_tile = btitle
            board.b_note = bnote
            board.b_writer = bwriter

            board.save()
            return redirect('/board')


    except Board.DoesNotExist:
        return Response({"success": False, "msg": "게시글 없음"})

def board_delete(request):
    bno = request.GET['b_no']
    Board.objects.get(b_no=bno).delete()

    return redirect('/board')


def ds_querytolist(request):

    rsBoard = Board.objects.all()

    print("Type of model query result : ")
    print(type(rsBoard))

    rsList = []

    for record in rsBoard:
        lst = list(record.b_title)
        rsList.append(lst)

    print("Type of list : ")
    print(type(rsList))
    print(rsList)

    return render(request, "datastudy.html", {})

def ds_orm(request):
    rsBoard = Board.objects.all()
    print(type(rsBoard))

    rsBoard2 = Board.objects.raw('SELECT * FROM board')
    print(type(rsBoard2))

    with connection.cursor() as cursor0:
        cursor0.execute('SELECT * FROM board')
        rsBoard3 = cursor0.fetchall()
        cursor0.close
    print(type(rsBoard3))

    dbCon = pymysql.connect('localhost', 'root', 'root', 'edudb')
    cursor1 = dbCon.cursor()
    cursor1.execute('SELECT * FROM board')
    rsBoard4 = cursor1.fetchall()
    sursor1.close

    print(type(rsBoard4))

    return render(request, 'ds_orm.html', {
        'rsBoard': rsBoard,
        'rsBoard2': rsBoard2,
        'rsBoard3': rsBoard3,
        'rsBoard4': rsBoard4,
    })

def markdown2(request):
    return render(request, "markdown2.html")