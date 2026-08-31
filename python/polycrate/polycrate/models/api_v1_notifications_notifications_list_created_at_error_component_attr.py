from typing import Literal

ApiV1NotificationsNotificationsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsNotificationsListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_notifications_notifications_list_created_at_error_component_attr(
    value: str,
) -> ApiV1NotificationsNotificationsListCreatedAtErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
