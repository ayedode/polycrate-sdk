from typing import Literal

ApiV1NotificationsNotificationsListStateErrorComponentAttr = Literal["state"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsNotificationsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_notifications_notifications_list_state_error_component_attr(
    value: str,
) -> ApiV1NotificationsNotificationsListStateErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
