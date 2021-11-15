from django.shortcuts import render

# Create your views here.
def services(request):
    context = {'skill':'active'}
    return render(request,'serv/services.html')

# view function python that take a web