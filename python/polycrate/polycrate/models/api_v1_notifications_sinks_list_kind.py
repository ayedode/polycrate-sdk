from typing import Literal

ApiV1NotificationsSinksListKind = Literal["email", "mattermost", "msteams", "slack"]

API_V1_NOTIFICATIONS_SINKS_LIST_KIND_VALUES: set[ApiV1NotificationsSinksListKind] = {
    "email",
    "mattermost",
    "msteams",
    "slack",
}


def check_api_v1_notifications_sinks_list_kind(value: str) -> ApiV1NotificationsSinksListKind:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_KIND_VALUES!r}")
