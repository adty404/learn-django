from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {'title': 'A First Meetup', 'location': 'London', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'},
    ]

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })
