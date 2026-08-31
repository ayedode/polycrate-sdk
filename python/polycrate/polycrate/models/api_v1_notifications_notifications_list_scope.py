from typing import Literal

ApiV1NotificationsNotificationsListScope = Literal["system", "user"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_VALUES: set[ApiV1NotificationsNotificationsListScope] = {
    "system",
    "user",
}


def check_api_v1_notifications_notifications_list_scope(value: str) -> ApiV1NotificationsNotificationsListScope:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_VALUES!r}"
    )
