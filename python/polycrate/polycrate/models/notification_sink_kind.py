from typing import Literal

NotificationSinkKind = Literal["email", "mattermost", "msteams", "slack"]

NOTIFICATION_SINK_KIND_VALUES: set[NotificationSinkKind] = {
    "email",
    "mattermost",
    "msteams",
    "slack",
}


def check_notification_sink_kind(value: str) -> NotificationSinkKind:
    if value in NOTIFICATION_SINK_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_KIND_VALUES!r}")
