from django.shortcuts import render
from django.http import HttpResponse
import datetime

from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar

# a request to display the current time on a web page
def current_datetime(request):

    now = datetime.datetime.now()

    response = """ 
    <html>
     <title>The current time</title>
     <body>
     <h1> It's %s. </h1>  
     </body>  
    </html>
    """

    response = response % (now,)

    return HttpResponse(response)

def home(request):
    return render(request, "home.html")

def carousel_demo(request):
    return render(request, "carousel.html")

def plotly_demo(request):
    x_data = [0, 1, 2, 3, 4, 5, 10, 15, 20, 33, 100, 500, 900]
    y_data = [4, 1, 1 ,16, 1, 1, 1, 5, 2, 3, 100, 5, 90]

    plot_div = plot([Bar(x=x_data, y=y_data,
                             name='Our First Graph in Plotly',
                             opacity=1.0, marker_color='blue')],
                    output_type='div', include_plotlyjs=False)

    return render(request, "plotly_demo.html", context={'plot_div': plot_div})

# demonstration of the contents of request objects
def display_request(request):
    for key in request.META:
        if key in ['SERVER_PROTOCOL', 'USER', 'PATH_INFO', 'QUERY_STRING', 'HTTP_USER_AGENT']:
            print(key, request.META[key])

        # if 'Chrome' in request.META['HTTP_USER_AGENT']:
        #     do X
        # elif 'Safari' in request.META['HTTP_USER_AGENT']:
        #     do Y
        # ...

    response = "Cooking ..."
    return HttpResponse(response)
