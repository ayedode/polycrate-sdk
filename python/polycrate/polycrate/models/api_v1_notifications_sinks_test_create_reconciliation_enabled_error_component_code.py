from typing import Literal

ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_test_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
