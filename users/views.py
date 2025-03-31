from django.shortcuts import render, redirect, get_object_or_404
from .models import  User, ForeignerLocation
from .forms import UserForm
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages

import os
import json
from django.conf import settings
from .models import UserLocation





def user_list(request):
    users = User.objects.all()
    form = UserForm()  # Initialize a blank form for adding a new user
    context = {'users': users, 'form': form}
    return render(request, 'users/user_list.html', context)

def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User saved successfully")
            return redirect('user_list')  # Redirect to the user list after successful save
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = UserForm()
    return render(request, "user_form.html", {"form": form})


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy






def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')
        else:
            messages.error(request, 'There was an error in the form.')
    else:
        form = UserForm(instance=user)
    context = {'form': form, 'user': user}  # Pass user instance to the template
    return render(request, 'users/user_form.html', context)

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})



def search_location(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            # Example: Searching for provinces by name
            provinces = UserLocation.objects.filter(name__icontains=query).values('id', 'name')
            return JsonResponse(list(provinces), safe=False)
        else:
            return JsonResponse({"error": "No query provided"}, status=400)
    return redirect('user_list')  
