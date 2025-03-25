from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})



def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return redirect('user_list')  # Just a fallback for any GET requests





def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('user_list') 
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)  # Handle the case where user does not exist
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)  # Ensure to pass request.FILES
        if form.is_valid():
            form.save()  # Save the updated user data
            return redirect('user_list')  
    else:
        form = UserForm(instance=user)  # Pre-fill the form with the current user data

    return render(request, 'users/user_form.html', {'form': form, 'user': user})

