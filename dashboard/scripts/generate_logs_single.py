# working ok, but needs more time. not bulk insertion

# Command for running the script:
# python manage.py runscript generate_logs  --script-args log


from datetime import datetime
from django.utils import timezone
import re

from django.contrib.auth.decorators import login_required
from django.db import transaction
from dashboard.models import LogHistory

@transaction.atomic
def run(*args):
    recordslist = []
    fp = open(args[0], 'r')
    lines = fp.readlines()
    for line in lines:
        if line:
            splitline = re.split(" ", line, 5)
            dt = str(datetime.today().year)+" "+ splitline[0]+ " "+splitline[1]+" "+ splitline[2]
            dt = datetime.strptime(dt, '%Y %b %d %H:%M:%S')
            x = re.search(r"(\[\d*\])?:$", splitline[4])
            cat = splitline[4][ :x.span()[0]]
            msg = splitline[5].rstrip('\n')
            log_instance = LogHistory.objects.create(datetime = dt, category = cat, message = msg)
            log_instance.save()
            
            # record = {"dt": dt, "cat": cat,"msg":msg}
            # recordslist.append(record)
            # print(dt, cat, msg)
    # return recordslist
