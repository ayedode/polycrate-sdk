from typing import Literal

NotificationSinkScope = Literal["system", "user"]

NOTIFICATION_SINK_SCOPE_VALUES: set[NotificationSinkScope] = {
    "system",
    "user",
}


def check_notification_sink_scope(value: str) -> NotificationSinkScope:
    if value in NOTIFICATION_SINK_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_SCOPE_VALUES!r}")
