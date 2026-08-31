from typing import Literal

NotificationKindEnum = Literal[
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

NOTIFICATION_KIND_ENUM_VALUES: set[NotificationKindEnum] = {
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


def check_notification_kind_enum(value: str) -> NotificationKindEnum:
    if value in NOTIFICATION_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_KIND_ENUM_VALUES!r}")
