from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Branch,District

from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'persons/apply.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/apply.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id)
    return render(request, 'persons/city_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'persons/register.html', {'form': form})


@login_required()
def profile(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, f' your application was submitted successfully')
        return redirect('home')

    return render(request, 'persons/apply.html', {'form': form})
