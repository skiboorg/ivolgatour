from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from tour.models import *
from django.contrib import messages

def index(request):
    allBanners = Banner.objects.filter(isActive=True).order_by('order')
    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    popularTours = Tour.objects.filter(isPopular=True)
    specialTours = Tour.objects.filter(isSpecial=True)
    popularDestinations = Country.objects.filter(isPopular=True)
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()

    # try:
    #     seotag = SeoTag.objects.first()
    #     pageTitle = seotag.indexTitle.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    #     pageDescription = seotag.indexDescription.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    #     pageKeywords = seotag.indexKeywords.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    # except:
    #     pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    #     pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    #     pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    homeActive = 'current-menu-item'
    return render(request, 'pages/index.html', locals())

def destinations(request):
    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    allDestinations = Country.objects.all()
    return render(request, 'pages/destinations.html', locals())

def contacts(request):
    allRegions = GlobalRegion.objects.all()
    allTypes = TourVariant.objects.all()
    newTours = Tour.objects.all()[:3]
    allTags = Tag.objects.all()
    return render(request, 'pages/contacts.html', locals())

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: locaclhost\nSitemap: localhost/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")
