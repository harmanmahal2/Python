from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST':
        #display blank reg form
        form = UserCreationForm()

    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            #log new  user in and redirect
            login(request, new_user)
            return redirect('learning_logs/index')

    #display a blank or invalid form
    context = {'form':form}
    return render(request, 'registration/register.html', context)