from typing import Literal

ApiV1NotificationsNotificationsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsNotificationsListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_notifications_list_scope_error_component_code(
    value: str,
) -> ApiV1NotificationsNotificationsListScopeErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
