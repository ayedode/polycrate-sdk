from typing import Literal

ApiV1IncidentsListStatus = Literal["contained", "investigating", "reported", "resolved", "reviewed"]

API_V1_INCIDENTS_LIST_STATUS_VALUES: set[ApiV1IncidentsListStatus] = {
    "contained",
    "investigating",
    "reported",
    "resolved",
    "reviewed",
}


def check_api_v1_incidents_list_status(value: str) -> ApiV1IncidentsListStatus:
    if value in API_V1_INCIDENTS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_STATUS_VALUES!r}")
