from typing import Literal

ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_test_create_enabled_model_types_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
