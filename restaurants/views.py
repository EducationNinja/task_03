from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "my_list": [
            {"restaurant_name": "Aroma", "food_type": "Italian, I think."},
            {"restaurant_name": "Tokyo", "food_type": "Japanese Food"},
            {"restaurant_name": "Fire Grill", "food_type": "Mexican Food"},
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {
        "my_object": {"restaurant_name": "Tokyo", "food_type": "Japanese Food"}
    }
    return render(request, 'detail.html', context)
