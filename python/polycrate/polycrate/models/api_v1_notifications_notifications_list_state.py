from typing import Literal

ApiV1NotificationsNotificationsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_VALUES: set[ApiV1NotificationsNotificationsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_notifications_notifications_list_state(value: str) -> ApiV1NotificationsNotificationsListState:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_VALUES!r}"
    )
