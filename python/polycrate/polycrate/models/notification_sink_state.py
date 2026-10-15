from typing import Literal

NotificationSinkState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTIFICATION_SINK_STATE_VALUES: set[NotificationSinkState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_notification_sink_state(value: str) -> NotificationSinkState:
    if value in NOTIFICATION_SINK_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_STATE_VALUES!r}")
