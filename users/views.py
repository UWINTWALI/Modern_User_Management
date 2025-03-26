from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Location
from .forms import UserForm
from django.http import JsonResponse

def search_location(request):
    query = request.GET.get('q', '')
    locations = Location.objects.filter(name__icontains=query).values('name')
    return JsonResponse(list(locations), safe=False)


def user_list(request):
    """Sort by first name (A-Z)"""
    users = User.objects.all().order_by('first_name')  
    return render(request, 'users/user_list.html', {'users': users})




def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return redirect('user_list')  



from django.db import IntegrityError

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            location_name = form.cleaned_data.get('location_name')

            if location_name:
                location_name = location_name.strip().lower()  # Normalize input

                try:
                    """Assign existing location or create a new one without duplication"""
                    location, created = Location.objects.get_or_create(
                        name__iexact=location_name,  # Case-insensitive search
                        defaults={"name": location_name}  # Ensures lowercase storage
                    )
                except IntegrityError:
                    """If IntegrityError occurs, fetch the existing location manually"""
                    location = Location.objects.filter(name__iexact=location_name).first()

                user.location = location  # Assign the correct location

            user.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'users/user_form.html', {'form': form})



from django.db import IntegrityError

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            location_name = form.cleaned_data.get('location_name')

            if location_name:
                location_name = location_name.strip().lower()  # Normalize input

                try:
                    """Try to get an existing location case-insensitively"""
                    location = Location.objects.filter(name__iexact=location_name).first()

                    if not location:
                        """If no matching location exists, create one"""
                        location = Location.objects.create(name=location_name)

                except IntegrityError:
                    """If IntegrityError occurs, fetch the existing location manually"""
                    location = Location.objects.filter(name__iexact=location_name).first()

                user.location = location  # Assign the correct location
            user.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'users/user_form.html', {'form': form, 'user': user})



def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'users/user_detail.html', {'user': user})


