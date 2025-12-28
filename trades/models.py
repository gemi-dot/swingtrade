from django.db import models
from django.utils import timezone

class PaperTrade(models.Model):
    symbol = models.CharField(max_length=10)
    entry = models.FloatField()
    stop = models.FloatField()
    target = models.FloatField()
    status = models.CharField(max_length=10, default="OPEN")
    pnl = models.FloatField(null=True, blank=True)
    opened_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(null=True, blank=True)

    def update_status(self, current_price):
        if self.status != "OPEN":
            return

        if current_price <= self.stop or current_price >= self.target:
            self.status = "CLOSED"
            self.closed_at = timezone.now()
            self.pnl = (current_price - self.entry) * 100
            self.save()


