from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            user_name = form.cleaned_data['user_name']
            address = form.cleaned_data['address']
            profile_pic = form.cleaned_data['profile_pic']
            # Add your logic here
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})