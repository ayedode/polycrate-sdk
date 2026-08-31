from typing import Literal

ApiV1NotificationsSinksUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateDebugModeErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
