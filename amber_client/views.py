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

    data = {}

    for each in res.json():
        if each["channelType"] != "general":
            continue

        if each["type"] == "CurrentInterval":
            data["now"] = each

        else:
            data.setdefault("future", []).append(each)

    return JsonResponse(data)
