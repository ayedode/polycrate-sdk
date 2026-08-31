from typing import Literal

ApiV1NotificationsSinksUpdateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_update_config_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateConfigErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
