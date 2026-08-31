from typing import Literal

ApiV1NotificationsSinksUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_notifications_sinks_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateDebugModeErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
