from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        "item1": "Игра A",
        "item2": "Игра B",
        "item3": "Игра C",
    }
    context = {"items": items}
    return render(request, 'third_task/shop.html', context)

def news(request):
    return render(request, 'third_task/news.html')