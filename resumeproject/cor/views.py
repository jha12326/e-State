from django.shortcuts import render
from .forms import CustomerForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer = form.save()
            name = Customer.fname + ' ' + Customer.lname
            messages.success(request, name + ":-" + ' your Form is successfully saved!.')
        else:    
            messages.warning(request, 'Sorry..! Form not saved.')
    else:
        form = CustomerForm()

    context = {'form':form}
    return render(request, 'cor/home.html', context)

def contact(request):
    context = {'contact':'active'}
    return render(request, 'cor/contact.html',context)