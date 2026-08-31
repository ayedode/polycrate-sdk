from typing import Literal

ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_discover_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
