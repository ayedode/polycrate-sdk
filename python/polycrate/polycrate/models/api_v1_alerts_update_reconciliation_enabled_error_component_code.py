from typing import Literal

ApiV1AlertsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
