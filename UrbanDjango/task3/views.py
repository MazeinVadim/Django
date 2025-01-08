from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def about(request):
    team_members = [
        {
            'name': 'Иван',
            'buttons': ['Кнопка 1', 'Кнопка 2'],
        },
        {
            'name': 'Мария',
            'buttons': ['Кнопка A', 'Кнопка B', 'Кнопка C'],
        },
        {
            'name': 'Петр',
            'buttons': ['Кнопка X'],
        },
    ]
    context = {
        'team_members': team_members,
    }
    return render(request, 'third_task/about.html', context)

def catalog(request):
    return render(request, 'third_task/catalog.html')

