from django.shortcuts import render

# Create your views here.
# webhooks/views.py
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from trades.models import PaperTrade

@csrf_exempt
def tradingview_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # Create paper trade
            PaperTrade.objects.create(
                symbol=data['symbol'],
                entry=float(data['price']),
                stop=float(data['stop']),
                target=float(data['target'])
            )
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "failed", "message": "Use POST method"})
