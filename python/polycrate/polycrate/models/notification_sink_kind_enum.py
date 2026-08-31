from typing import Literal

NotificationSinkKindEnum = Literal["email", "mattermost", "msteams", "slack"]

NOTIFICATION_SINK_KIND_ENUM_VALUES: set[NotificationSinkKindEnum] = {
    "email",
    "mattermost",
    "msteams",
    "slack",
}


def check_notification_sink_kind_enum(value: str) -> NotificationSinkKindEnum:
    if value in NOTIFICATION_SINK_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_KIND_ENUM_VALUES!r}")
