from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm

# creating a register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # saves form data when it is valid
            username = form.cleaned_data.get("username")
            # adding a flash message
            messages.success(request, f"Account created for {username}!")
            return redirect("blog-home")

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
