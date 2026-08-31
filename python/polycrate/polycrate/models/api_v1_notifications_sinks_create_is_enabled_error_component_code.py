from typing import Literal

ApiV1NotificationsSinksCreateIsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateIsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_create_is_enabled_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateIsEnabledErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
