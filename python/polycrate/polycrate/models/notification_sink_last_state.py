from typing import Literal

NotificationSinkLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTIFICATION_SINK_LAST_STATE_VALUES: set[NotificationSinkLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_notification_sink_last_state(value: str) -> NotificationSinkLastState:
    if value in NOTIFICATION_SINK_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_LAST_STATE_VALUES!r}")
