from typing import Literal

ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_partial_update_is_enabled_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
