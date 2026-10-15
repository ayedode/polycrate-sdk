from typing import Literal

NotificationSinkRequestKind = Literal["email", "mattermost", "msteams", "slack"]

NOTIFICATION_SINK_REQUEST_KIND_VALUES: set[NotificationSinkRequestKind] = {
    "email",
    "mattermost",
    "msteams",
    "slack",
}


def check_notification_sink_request_kind(value: str) -> NotificationSinkRequestKind:
    if value in NOTIFICATION_SINK_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_REQUEST_KIND_VALUES!r}")
