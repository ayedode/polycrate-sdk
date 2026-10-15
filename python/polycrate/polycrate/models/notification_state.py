from typing import Literal

NotificationState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTIFICATION_STATE_VALUES: set[NotificationState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_notification_state(value: str) -> NotificationState:
    if value in NOTIFICATION_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_STATE_VALUES!r}")
