from typing import Literal

ApiV1NotificationsSinksTestCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_test_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateDebugModeErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
