from django.shortcuts import render
from datetime import datetime
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Expense,Token, Income
# Create your views here.


@csrf_exempt
def submit_income(request):
    """" submits an income"""

   #TODO: validate date. user might be fake. Token might be fake. amount might be fake
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user=this_user, amount=request.POST['amount'],
        text=request.POST['text'], date=date)

    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_expense(request):
    """" submits an expense"""

   #TODO: validate date. user might be fake. Token might be fake. amount might be fake
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
        text=request.POST['text'], date=date)

    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder)