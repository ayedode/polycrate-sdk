from typing import Literal

NotificationLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTIFICATION_LAST_STATE_VALUES: set[NotificationLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_notification_last_state(value: str) -> NotificationLastState:
    if value in NOTIFICATION_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_LAST_STATE_VALUES!r}")
