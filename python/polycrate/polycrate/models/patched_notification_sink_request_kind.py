from typing import Literal

PatchedNotificationSinkRequestKind = Literal["email", "mattermost", "msteams", "slack"]

PATCHED_NOTIFICATION_SINK_REQUEST_KIND_VALUES: set[PatchedNotificationSinkRequestKind] = {
    "email",
    "mattermost",
    "msteams",
    "slack",
}


def check_patched_notification_sink_request_kind(value: str) -> PatchedNotificationSinkRequestKind:
    if value in PATCHED_NOTIFICATION_SINK_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_NOTIFICATION_SINK_REQUEST_KIND_VALUES!r}")
