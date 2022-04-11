from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV, BUS_STATIONS_LIST
import csv


with open(BUS_STATION_CSV, encoding='utf-8') as file:
    BUS_STATIONS_LIST += csv.DictReader(file)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations_view(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(BUS_STATIONS_LIST, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
