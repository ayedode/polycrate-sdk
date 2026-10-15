from typing import Literal

NotificationSinkListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTIFICATION_SINK_LIST_STATE_VALUES: set[NotificationSinkListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_notification_sink_list_state(value: str) -> NotificationSinkListState:
    if value in NOTIFICATION_SINK_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_LIST_STATE_VALUES!r}")
