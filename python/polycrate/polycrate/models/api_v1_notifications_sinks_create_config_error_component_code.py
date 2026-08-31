from typing import Literal

ApiV1NotificationsSinksCreateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_create_config_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateConfigErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
