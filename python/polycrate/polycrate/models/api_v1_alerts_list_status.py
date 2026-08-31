from typing import Literal

ApiV1AlertsListStatus = Literal["firing", "open", "pending", "resolved", "silenced"]

API_V1_ALERTS_LIST_STATUS_VALUES: set[ApiV1AlertsListStatus] = {
    "firing",
    "open",
    "pending",
    "resolved",
    "silenced",
}


def check_api_v1_alerts_list_status(value: str) -> ApiV1AlertsListStatus:
    if value in API_V1_ALERTS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_STATUS_VALUES!r}")
