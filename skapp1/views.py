from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,Http404

from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def index(request):
    company = 'Outdoor Equipment'
    ordered_warranty = False
    ship_date = datetime.date(2009, 4, 2)
    person_name = 'John Smith'
    item_list = [1,2,3,4,5]
    
   
    return render(request, 'skapp1/index.html', locals())
