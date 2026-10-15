from typing import Literal

NotificationScope = Literal["system", "user"]

NOTIFICATION_SCOPE_VALUES: set[NotificationScope] = {
    "system",
    "user",
}


def check_notification_scope(value: str) -> NotificationScope:
    if value in NOTIFICATION_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SCOPE_VALUES!r}")
