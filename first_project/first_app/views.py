from django.shortcuts import render

# Create your views here.
def index(request):
    value = "Hello Randstad"
    return render(request, 'index.html', context={"value": value})

def home(request):
    name = 'Ichiro Randstad'
    fruits = ['strawberry', 'apple', 'grapes']
    info = {
        'my_name': 'Ichiro',
        'age': 20
    }
    return render(request, 'home.html', context={
        'name': name,
        'fruits': fruits,
        'info': info,
    })

def athlete_profile(request):
    athlete = {
        'name': 'Yuta',
        'gender': 'male',
        'age': 17
    }
    return render(request, 'profile.html', context={'athlete': athlete})

def sample1(request):
    return render(request, 'sample1.html')
