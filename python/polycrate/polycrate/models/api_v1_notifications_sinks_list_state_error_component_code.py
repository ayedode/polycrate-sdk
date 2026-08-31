from typing import Literal

ApiV1NotificationsSinksListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_SINKS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_sinks_list_state_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksListStateErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
