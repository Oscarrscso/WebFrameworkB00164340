from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import Group
# Create your views here.


def signup_page(request):
    if request.method == "POST":

        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            group = Group.objects.get(name="Customer")
            user = signup_form.save()
            user.groups.add(group)
            login(request, user)
            return redirect("catalog_page_sorted")
    elif request.method == "GET":
            signup_form = UserCreationForm()

    context = {"signup_form": signup_form}
    return render (request, "accounts/signup.html", context)


def login_page(request):
    if request.method == "POST":

        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("catalog_page_sorted")
    elif request.method == "GET":
            login_form = AuthenticationForm(request)
    

    context = {"login_form": login_form}
    return render (request, "accounts/login.html", context)


def logout_page(request):
    logout(request)
    return redirect("catalog_page_sorted")
