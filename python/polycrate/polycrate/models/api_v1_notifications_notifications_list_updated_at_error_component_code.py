from typing import Literal

ApiV1NotificationsNotificationsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsNotificationsListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_notifications_list_updated_at_error_component_code(
    value: str,
) -> ApiV1NotificationsNotificationsListUpdatedAtErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
