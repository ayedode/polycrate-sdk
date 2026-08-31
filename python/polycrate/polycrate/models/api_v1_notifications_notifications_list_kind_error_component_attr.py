from typing import Literal

ApiV1NotificationsNotificationsListKindErrorComponentAttr = Literal["kind"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsNotificationsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_notifications_notifications_list_kind_error_component_attr(
    value: str,
) -> ApiV1NotificationsNotificationsListKindErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
