from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserLocationForm, ForeignerLocationForm
from .models import User, UserLocation, ForeignerLocation
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from django.db.models import Q


def detail_user(request, userid):
    user = get_object_or_404(User, userid=userid)
    context = { 'user':user }
    return render(request, 'users/user_details.html', context)


def search_location(request):
    query = request.GET.get('q', '').strip().lower()  # Ensure clean input
    suggested_foreign_location = ForeignerLocation.objects.filter(foreign_location__icontains=query).values('foreign_location')
    return JsonResponse(list(suggested_foreign_location), safe=False)

""" LIST REGISTERED USERS VIEW___________________________________________________________________________________________________"""
def list_users(request):
    users = User.objects.all()
    return render(request, 'users/list_users.html', {'users': users})

""" REGISTER NEW USERS VIEW____________________________________________________________________________________________________"""
def user_create(request):
    users = User.objects.all()
    if request.method == 'POST':
        print("POST data:", request.POST)  # Debug
        print("FILES data:", request.FILES)  # Debug
        
        user_form = UserForm(request.POST, request.FILES)
        location_form = UserLocationForm(request.POST)
        foreigner_form = ForeignerLocationForm(request.POST)
        
        print("User form is valid:", user_form.is_valid()) 
        if not user_form.is_valid():
            print("User form errors:", user_form.errors) 
            
        print("Location form is valid:", location_form.is_valid())
        if not location_form.is_valid():
            print("Location form errors:", location_form.errors)  
            
        print("Foreigner form is valid:", foreigner_form.is_valid())  
        if not foreigner_form.is_valid():
            print("Foreigner form errors:", foreigner_form.errors)  
        
        # Always attempt to save user and handle locations more flexibly
        if user_form.is_valid():
            user = user_form.save(commit=False)
            is_foreigner = user_form.cleaned_data.get('is_foreigner', False)
            
            # Set both location relationships to None initially
            user.location = None
            user.foreign_location = None
            
            # Now handle the appropriate location based on is_foreigner flag
            if is_foreigner:
                if foreigner_form.is_valid() and foreigner_form.cleaned_data.get('foreign_location'):
                    foreign_location = foreigner_form.save()
                    user.foreign_location = foreign_location
            else:
                if location_form.is_valid():
                    # Don't require all location fields
                    location = location_form.save()
                    user.location = location
            
            # Save the user regardless of location status
            user.save()
            print("User saved with ID:", user.id)  # Debug
            return redirect('list_users')
    else:
        user_form = UserForm()
        location_form = UserLocationForm()
        foreigner_form = ForeignerLocationForm()

    return render(request, 'users/user_form.html', {
        'user_form': user_form, 
        'location_form': location_form,
        'foreigner_form': foreigner_form,
        'users':users
    })



""" EDIT VIEW____________________________________________________________________________________________________________________________"""

def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)
        
        # Handle the case when location might be None
        if user.location:
            location_form = UserLocationForm(request.POST, instance=user.location)
        else:
            location_form = UserLocationForm(request.POST)
            
        # Handle the case when foreign_location might be None
        if user.foreign_location:
            foreigner_form = ForeignerLocationForm(request.POST, instance=user.foreign_location)
        else:
            foreigner_form = ForeignerLocationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            is_foreigner = user_form.cleaned_data['is_foreigner']
            
            if is_foreigner:
                if foreigner_form.is_valid() and foreigner_form.cleaned_data['foreign_location']:
                    if user.foreign_location:
                        # Update existing foreigner location
                        foreigner_location = foreigner_form.save()
                    else:
                        # Create new foreigner location
                        foreigner_location = foreigner_form.save()
                        user.foreign_location = foreigner_location
                    
                    # Clear local location if switching to foreigner
                    if user.location:
                        location_to_delete = user.location
                        user.location = None
                        user.save()
                        location_to_delete.delete()
                    else:
                        user.location = None
            else:
                if location_form.is_valid() and location_form.cleaned_data['country']:
                    if user.location:
                        # Update existing location
                        location = location_form.save()
                    else:
                        # Create new location
                        location = location_form.save()
                        user.location = location
                    
                    # Clear foreign location if switching to local
                    if user.foreign_location:
                        foreign_to_delete = user.foreign_location
                        user.foreign_location = None
                        user.save()
                        foreign_to_delete.delete()
                    else:
                        user.foreign_location = None

            user.save()
            return redirect('list_users')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm(instance=user)
        location_form = UserLocationForm(instance=user.location) if user.location else UserLocationForm()
        foreigner_form = ForeignerLocationForm(instance=user.foreign_location) if user.foreign_location else ForeignerLocationForm()

    return render(request, 'users/user_form.html', {
        'user_form': user_form,
        'location_form': location_form,
        'foreigner_form': foreigner_form,
        'user_id': user_id,
    })


""" DELETE VIEW_________________________________________________________________________________________________________________"""

def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    return render(request, 'users/user_confirm_delete.html', {'user': user})


