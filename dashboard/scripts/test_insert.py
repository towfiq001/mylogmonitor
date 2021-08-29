# scripts/generate_logs.py

from datetime import datetime

from django.contrib.auth.decorators import login_required
from dashboard.models import LogHistory

def run():
    log_instance = LogHistory.objects.create(datetime= datetime.today(), category='1', message='1')
    log_instance.save()
    print(datetime.today())
    print(log_instance)