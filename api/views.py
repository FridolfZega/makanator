from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def play(request):
    return render(request, 'play.html')

def howtoplay(request):
    return render(request, 'howtoplay.html')

def trueorfalse(request):
    return render(request, 'trueorfalse.html')

def result_true(request):
    return render(request, 'result_true.html')
