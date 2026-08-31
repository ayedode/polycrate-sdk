from typing import Literal

ApiV1NotificationsSinksListScope = Literal["system", "user"]

API_V1_NOTIFICATIONS_SINKS_LIST_SCOPE_VALUES: set[ApiV1NotificationsSinksListScope] = {
    "system",
    "user",
}


def check_api_v1_notifications_sinks_list_scope(value: str) -> ApiV1NotificationsSinksListScope:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_SCOPE_VALUES!r}")
