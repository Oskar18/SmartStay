from django.shortcuts import render

def home(request):
    return render(request, 'checkin/home.html')
