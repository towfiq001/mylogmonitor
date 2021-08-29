# scripts/delete_all_logs.py

from dashboard.models import LogHistory

def run():
    logs = LogHistory.objects.all()
    logs.delete()