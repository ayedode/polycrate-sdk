from typing import Literal

ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
