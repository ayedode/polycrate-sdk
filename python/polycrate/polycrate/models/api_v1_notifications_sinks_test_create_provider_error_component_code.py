from typing import Literal

ApiV1NotificationsSinksTestCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notifications_sinks_test_create_provider_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateProviderErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
