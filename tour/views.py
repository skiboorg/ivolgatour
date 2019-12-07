from django.shortcuts import render, get_object_or_404
from .models import *

def showtour_by_type(request, type):
    tourType = get_object_or_404(TourVariant, nameSlug=type)
    allToursbyType = Tour.objects.filter(variant=tourType)

    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()

    tourtypeactive = 'active'
    return render(request, 'pages/tourtype.html', locals())


def showtour_by_destination(request, country):
    destination = get_object_or_404(Country, nameSlug=country)
    allToursbyDestination = Tour.objects.filter(country=destination)

    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()

    tourtypeactive = 'active'
    return render(request, 'pages/tourdestination.html', locals())

def showtour_by_globalregion(request,region):
    region = get_object_or_404(GlobalRegion, nameSlug=region)
    allCountries = Country.objects.filter(globalRegion=region)
    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()

    tourtypeactive = 'active'
    return render(request, 'pages/tourglobalregion.html', locals())

def showalltours(request):
    allTours = Tour.objects.all()
    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()
    return render(request, 'pages/alltours.html', locals())


def tour(request,slug):
    tour = get_object_or_404(Tour, nameSlug=slug)
    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()
    return render(request, 'pages/tour.html', locals())


