from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import requests


def forecast(request):
    res = requests.get(
        f"https://api.amber.com.au/v1/sites/{settings.AMBER_LOCATION_ID}/prices/current",
        params={"next": 12, "previous": 0},
        headers={"Authorization": f"Bearer {settings.AMBER_API_KEY}"},
    )
    res.raise_for_status()

    data = res.json()

    return JsonResponse(data, safe=False)
