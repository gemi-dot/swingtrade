
# Create your models here.

from django.db import models
from django.utils import timezone

class TradingSignal(models.Model):
    SIGNAL_CHOICES = [
        ("BUY", "Buy"),
        ("SELL", "Sell"),
        ("HOLD", "Hold"),
    ]

    symbol = models.CharField(max_length=10)
    sma_fast = models.FloatField()
    sma_slow = models.FloatField()
    signal = models.CharField(max_length=4, choices=SIGNAL_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.symbol} - {self.signal}"



class DailyCandle(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('symbol', 'date')

    def __str__(self):
        return f"{self.symbol} - {self.date}"
