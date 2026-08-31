from typing import Literal

ApiV1NotificationsNotificationsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsNotificationsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_notifications_list_created_at_error_component_code(
    value: str,
) -> ApiV1NotificationsNotificationsListCreatedAtErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
