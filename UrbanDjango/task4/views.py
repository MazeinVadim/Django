from django.shortcuts import render

def index(request):
    return render(request, 'fourth_task/index.html')

def about(request):
    games = ["Atomic Heart", "Cyberpunk 2077", "Elden Ring"]
    context = {
        'games': games,  # Теперь передаем список игр
    }
    return render(request, 'fourth_task/about.html', context)


def catalog(request):
    return render(request, 'fourth_task/catalog.html')