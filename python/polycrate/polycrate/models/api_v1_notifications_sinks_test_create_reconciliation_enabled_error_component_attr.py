from typing import Literal

ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_notifications_sinks_test_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
