from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import LogHistory
from django.db.models import Count
import json



@login_required
def index(request):
    """View function for home page of site."""    
    # return HttpResponse("Hello, world. You're at the log dashboard.")

    num_logs = LogHistory.objects.count()
    chart_one = LogHistory.objects.values('datetime').annotate(Count('id')).order_by('datetime')
    chart_two = LogHistory.objects.values('category').annotate(Count('id')).order_by('category')
    table_data = LogHistory.objects.order_by('-datetime')[:10]

    # num_logs = LogByDate.objects.count()
    # chart_one = LogByDate.objects.values('date').annotate(Count('id'))
    # chart_two = LogByDate.objects.values('category').annotate(Count('id'))

    x_c1= []
    y_c1= []
    x_c2= []
    y_c2= []
    c2_data = []

    for item in chart_one:
        x_c1.append(item['datetime'].strftime("%b %d %H:%M:%S"))
        # x_c1.append(item['date'].strftime("%b %d"))
        y_c1.append(item['id__count'])

    for item in chart_two:
        x_c2.append(item['category'])
        y_c2.append(item['id__count'])
        piefield = {'name': item['category'], 'y': item['id__count']}
        c2_data.append(piefield)
    
    context = {
        'num_logs': num_logs,
        'x_c1' : json.dumps(x_c1),
        'y_c1' : json.dumps(y_c1),
        # 'x_c2' : json.dumps(x_c2),
        # 'y_c2' : json.dumps(y_c2),
        'piedata' : json.dumps(c2_data),
        'tabledata' : table_data,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
