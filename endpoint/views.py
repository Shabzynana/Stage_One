from django.shortcuts import render
from http import HTTPStatus
from django.http import JsonResponse
from django.views import View
from datetime import datetime
import pytz

def index(request):
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    # Get current UTC time
    utc_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    response = {
        "slack_name": slack_name,
        "current_day": datetime.now().strftime("%A"),
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Shabzynana/Stage_One/blob/main/endpoint/views.py",
        "github_repo_url": "https://github.com/Shabzynana/Stage_One",
        "status_code": HTTPStatus.OK,
    }

    return JsonResponse(response)
