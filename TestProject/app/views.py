from django.shortcuts import render
from django.http import HttpResponse


from .models import Tour,Tourist,Location,Review


def getTours(request):
    tours = Tour.objects.all()


    return render(request, 'tours.html', {'tours' : tours})

def getTourists(request):
    tourists = Tourist.objects.all()


    return render(request, 'tourists.html', {'tourists': tourists})


def getTourByName(request, name):
    tour = Tour.objects.all().filter(name=name)
    # if name := request.GET.get('name'):
    #     tour = tour.filter(name=name)

    # tour = tour.all()


    return render(request, 'tour.html', {'tour':tour})

def getReviews(request):
    reviews = Review.objects.all()

    return render(request, 'reviews.html', {'reviews': reviews})


