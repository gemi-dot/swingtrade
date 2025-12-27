from django.core.management.base import BaseCommand
import pandas as pd
from market.models import DailyCandle
from market.signal_engine import generate_daily_signal

class Command(BaseCommand):
    help = "Scan AAPL daily and generate signals"

    def handle(self, *args, **kwargs):
        qs = DailyCandle.objects.filter(symbol="AAPL").order_by('date')
        df = pd.DataFrame(list(qs.values()))
        if df.empty:
            self.stdout.write("No data yet. Fetch data first.")
            return

        result = generate_daily_signal(df)
        self.stdout.write(str(result))
