from django.http import HttpResponse


# Create your views here.
# Whenever user requests something views are going to return them same

def index(request):
    return HttpResponse("<h1>This is Rahul Yadav !</h1>")
