from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm

# creating a register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # saves form data when it is valid
            username = form.cleaned_data.get("username")
            # adding a flash message
            messages.success(request, f"{username}'s account has been created. You are now able to log in.")
            return redirect("login")

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# creating a profile view
@login_required
def profile(request):
    return render(request, "users/profile.html")