from datetime import datetime
import re
from django.contrib.auth.decorators import login_required
from django.db import transaction
from dashboard.models import LogHistory

@transaction.atomic
def run(*args):
    recordslist = []
    fp = open(args[0], 'r')
    fpout = open('out.txt', 'w')
    lines = fp.readlines()
    max_chunk_size = 100
    len_lines = len(lines)
    index_lines = 0
    for line in lines:
        if line:
            splitline = re.split(" ", line, 5)
            dt = str(datetime.today().year)+" "+ splitline[0]+ " "+splitline[1]+" "+ splitline[2]
            dt = datetime.strptime(dt, '%Y %b %d %H:%M:%S')
            x = re.search(r"(\[\d*\])?:$", splitline[4])
            cat = splitline[4][ :x.span()[0]]
            msg = splitline[5].rstrip('\n')     
            record = LogHistory(datetime = dt, category = cat, message = msg)
            recordslist.append(record)
            # insert into database 100 logs at a time.
            if len(recordslist) == max_chunk_size:
                LogHistory.objects.bulk_create(recordslist)
                recordslist.clear() # clears all the items from the list
        index_lines += 1
        if index_lines == len_lines:
            LogHistory.objects.bulk_create(recordslist)
            recordslist.clear() # clears all the items from the list
    print(index_lines)

    