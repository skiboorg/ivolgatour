from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def index(request):
    #allBanners = Banner.objects.filter(isActive=True).order_by('order')
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

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: locaclhost\nSitemap: localhost/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")
