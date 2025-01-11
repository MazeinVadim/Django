from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ["Vladislav Ivanov", "Vladimir Pugachov", "Marina Sokolova"]


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                info['form'] = form
                return render(request, "fifth_task/registration_page.html", info)
            elif int(age) < 18:
                info['error'] = 'Возраст должен быть не менее 18'
                info['form'] = form
                return render(request, "fifth_task/registration_page.html", info)
            elif username in users:
                info['error'] = 'Пользователь с таким именем уже существует'
                info['form'] = form
                return render(request, "fifth_task/registration_page.html", info)
            else:
                return HttpResponse(f"Приветствуем, {username}!")
        else:
            info['form'] = form
            return render(request, "fifth_task/registration_page.html", info)
    else:
        info['form'] = UserRegister()
        return render(request, "fifth_task/registration_page.html", info)


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, "fifth_task/registration_page.html", info)
        elif int(age) < 18:
            info['error'] = 'Возраст должен быть не менее 18'
            return render(request, "fifth_task/registration_page.html", info)
        elif username in users:
            info['error'] = 'Пользователь с таким именем уже существует'
            return render(request, "fifth_task/registration_page.html", info)
        else:
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "fifth_task/registration_page.html", info)