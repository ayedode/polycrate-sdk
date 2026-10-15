from typing import Literal

NotificationListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTIFICATION_LIST_STATE_VALUES: set[NotificationListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_notification_list_state(value: str) -> NotificationListState:
    if value in NOTIFICATION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_LIST_STATE_VALUES!r}")
