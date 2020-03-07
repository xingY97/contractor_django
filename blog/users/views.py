from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.Post)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()

    context = {'form':form}

    return render(request, 'users/register.html', context)


