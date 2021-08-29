# scripts/delete_all_logs.py

from dashboard.models import LogHistory

def run():
    logs = LogHistory.objects.all()
    for log_instance in logs:
        print(log_instance)