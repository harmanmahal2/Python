from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST':
        #display blank registration form
        form = UserCreationForm()

    else:
        #process the form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #log the user in and redirect to home
            login(request, new_user)
            return redirect('match_results:index')

    #display a blank form
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

