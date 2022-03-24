from django.shortcuts import render

# Create your views here.
def jinjo(request):
    d={'x':'YADAV'}
    return render(request,'jinjo.html',d)


def ifcondition(request):
    d1={'a':40}
    return render(request,'ifcondition.html',d1)
