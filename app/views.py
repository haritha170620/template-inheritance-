from django.shortcuts import render

# Create your views here.
def mdb5(request):
    return render(request,'mdb5.html')

def child1(request):
    return render(request,'child1.html')

def child2(request):
    return render(request,'child2.html')
