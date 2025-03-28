from django.shortcuts import render, redirect, get_object_or_404
from .models import Province, District, Sector, Cell, Village, User
from .forms import UserForm
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages


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



class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "user_form.html"
    success_url = reverse_lazy("user_list")  # Redirect after success



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


def get_provinces(request, country_id):
    provinces = Province.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse({'provinces': list(provinces)})

def get_districts(request, province_id):
    districts = District.objects.filter(province_id=province_id).values('id', 'name')
    return JsonResponse({'districts': list(districts)})

def get_sectors(request, district_id):
    sectors = Sector.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse({'sectors': list(sectors)})

def get_cells(request, sector_id):
    cells = Cell.objects.filter(sector_id=sector_id).values('id', 'name')
    return JsonResponse({'cells': list(cells)})

def get_villages(request, cell_id):
    villages = Village.objects.filter(cell_id=cell_id).values('id', 'name')
    return JsonResponse({'villages': list(villages)})




def search_location(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            # Example: Searching for provinces by name
            provinces = Province.objects.filter(name__icontains=query).values('id', 'name')
            return JsonResponse(list(provinces), safe=False)
        else:
            return JsonResponse({"error": "No query provided"}, status=400)
    return redirect('home')  # Redirect to home or another appropriate page
