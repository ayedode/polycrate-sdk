from typing import Literal

ApiV1NotificationsNotificationsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsNotificationsListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_notifications_list_state_error_component_code(
    value: str,
) -> ApiV1NotificationsNotificationsListStateErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_NOTIFICATIONS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
