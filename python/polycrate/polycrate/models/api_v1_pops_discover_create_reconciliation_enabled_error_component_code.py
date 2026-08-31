from typing import Literal

ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_POPS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pops_discover_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_POPS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
