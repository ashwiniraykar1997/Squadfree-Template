from django.shortcuts import render

from .models import Feedback




# Create your views here.
# Create your views here.
def index(request):
    fed = Feedback.objects.all()

    return render(request,'index.html',{'fed':fed})