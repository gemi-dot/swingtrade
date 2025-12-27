from django.db import models

# Create your models here.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from trades.models import PaperTrade

@csrf_exempt
def tradingview_webhook(request):
    data = json.loads(request.body)
    PaperTrade.objects.create(
        symbol=data['symbol'],
        entry=data['price'],
        stop=data['stop'],
        target=data['target']
    )
    return JsonResponse({"status": "ok"})
