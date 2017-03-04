from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_expense(request):
    """"user submits an expense"""
   #TODO: validate date. user might be fake. Token might be fake. amount might be fake
   this_token = request.POST.['token']
   this_user = User.objects.filter(token__token = this_token).get()
   now = datetime.now()
   Expense.objects.create(user=this_user, amount=request.POST['amount'],
            text=request.POST['text'], date=now)

    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder)