from django.shortcuts import render
from trades.models import PaperTrade
from market.models import TradingSignal

# Create your views here.
# trades/views.py

def dashboard(request):
    trades = PaperTrade.objects.all().order_by("-opened_at")
    signals = TradingSignal.objects.all().order_by("-created_at")[:10]

    return render(request, "trades/dashboard.html", {
        "trades": trades,
        "signals": signals,
    })