from typing import Literal

ApiV1NotificationsNotificationsListScopeErrorComponentAttr = Literal["scope"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsNotificationsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_notifications_notifications_list_scope_error_component_attr(
    value: str,
) -> ApiV1NotificationsNotificationsListScopeErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
