from typing import Literal

ApiV1NotificationsNotificationsListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsNotificationsListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_notifications_list_kind_error_component_code(
    value: str,
) -> ApiV1NotificationsNotificationsListKindErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
