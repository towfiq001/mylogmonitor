from dashboard.models import LogHistory

def run():
    logcounts = LogHistory.objects.all()
    print(logcounts)