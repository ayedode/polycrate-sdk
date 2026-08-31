from typing import Literal

ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_update_is_system_default_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
