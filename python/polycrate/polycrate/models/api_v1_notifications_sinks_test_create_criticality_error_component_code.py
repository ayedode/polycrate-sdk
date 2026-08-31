from typing import Literal

ApiV1NotificationsSinksTestCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_sinks_test_create_criticality_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateCriticalityErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
