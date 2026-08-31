from typing import Literal

ApiV1NotificationsSinksCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_NOTIFICATIONS_SINKS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_notifications_sinks_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateDebugModeErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
