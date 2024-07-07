import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from fastapi import FastAPI, Depends
from fast_api.schemas import Schema
from fast_api.models import EndpointStates, ClientInfo
from django.utils import timezone


app = FastAPI()


@app.post("/filter-endpoints/")
def filter_endpoints(payload: Schema):
    from django.db.models import Q

    input_start = payload.input_start
    endpoint_id = 139

    # Найти все записи из endpoint_state где state_start >= input_start и endpoint_id = 139
    states = EndpointStates.objects.filter(
        Q(state_start__gte=input_start.timestamp() * 1000000) &
        Q(endpoint_id=endpoint_id)
    ).order_by('-state_start')

    # Из данных, полученных выше, найти все записи, где id строки кратен числу 3
    states_filtered = [state for state in states if int(state.id) % 3 == 0]

    if len(states_filtered) >= 3:
        third_record = states_filtered[2]
        client_info = third_record.client.client_info.info
        state_id = third_record.state_id
    else:
        client_info = None
        state_id = None

    return {
        "filtered_count": len(states_filtered),
        "client_info": client_info,
        "state_id": state_id
    }