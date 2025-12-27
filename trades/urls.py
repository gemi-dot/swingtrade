from django.urls import path
from trades.views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
