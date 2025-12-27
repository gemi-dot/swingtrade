# trades/management/commands/update_trades.py
from django.core.management.base import BaseCommand
from trades.models import PaperTrade
import yfinance as yf

class Command(BaseCommand):
    help = "Update all open paper trades and calculate PnL"

    def handle(self, *args, **kwargs):
        open_trades = PaperTrade.objects.filter(status="OPEN")
        for trade in open_trades:
            # Fetch latest price from Yahoo Finance
            data = yf.download(trade.symbol, period="1d", interval="1d")
            if not data.empty:
                #current_price = data['Close'].iloc[-1]
                current_price = float(data['Close'].iloc[-1])
                trade.update_status(current_price)
                self.stdout.write(f"Updated {trade.symbol}: Status={trade.status}, PnL={trade.pnl}")
