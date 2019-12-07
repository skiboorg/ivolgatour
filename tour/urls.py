from django.urls import path
from . import views



urlpatterns = [
    # path('', views.index, name='index'),
    # path('tag/<tag>', views.showtour_by_tag, name='showtour_by_tag'),
    path('type/<type>', views.showtour_by_type, name='showtour_by_type'),
    path('destination/<country>', views.showtour_by_destination, name='showtour_by_destination'),
    path('global/<region>', views.showtour_by_globalregion, name='showtour_by_globalregion'),
    path('all/', views.showalltours, name='showalltours'),
    path('<slug>', views.tour, name='showtour'),



]