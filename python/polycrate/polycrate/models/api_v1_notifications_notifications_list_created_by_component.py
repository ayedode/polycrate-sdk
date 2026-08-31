from typing import Literal

ApiV1NotificationsNotificationsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1NotificationsNotificationsListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_notifications_notifications_list_created_by_component(
    value: str,
) -> ApiV1NotificationsNotificationsListCreatedByComponent:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
