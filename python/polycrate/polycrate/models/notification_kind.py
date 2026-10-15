from typing import Literal

NotificationKind = Literal[
    "alert",
    "downtime",
    "generic",
    "info",
    "maintenance",
    "note_created",
    "note_reminder",
    "note_reply",
    "note_resolved",
    "recovery",
    "warning",
]

NOTIFICATION_KIND_VALUES: set[NotificationKind] = {
    "alert",
    "downtime",
    "generic",
    "info",
    "maintenance",
    "note_created",
    "note_reminder",
    "note_reply",
    "note_resolved",
    "recovery",
    "warning",
}


def check_notification_kind(value: str) -> NotificationKind:
    if value in NOTIFICATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_KIND_VALUES!r}")
