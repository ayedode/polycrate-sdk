from typing import Literal

ApiV1NotificationsNotificationsListKind = Literal[
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

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_VALUES: set[ApiV1NotificationsNotificationsListKind] = {
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


def check_api_v1_notifications_notifications_list_kind(value: str) -> ApiV1NotificationsNotificationsListKind:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_VALUES!r}"
    )
