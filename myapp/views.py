from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def timer_page(request):
    return render(request, 'timer.html')