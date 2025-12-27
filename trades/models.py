
from django.db import models
from datetime import datetime
from django.utils import timezone

class PaperTrade(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
    ]

    symbol = models.CharField(max_length=10)
    entry = models.FloatField()
    stop = models.FloatField()
    target = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="OPEN")
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    pnl = models.FloatField(default=0.0)

    def update_status(self, current_price):
        """
        Automatically close trade if current price hits stop or target
        """
        if self.status == "OPEN":
            if current_price <= self.stop:
                self.status = "CLOSED"
                self.pnl = current_price - self.entry
                self.closed_at = datetime.now()  # ✅ inside method
                self.save()
            elif current_price >= self.target:
                self.status = "CLOSED"
                self.pnl = current_price - self.entry
                self.closed_at = datetime.now()  # ✅ inside method
                self.save()

    def __str__(self):
        return f"{self.symbol} - {self.status}"
