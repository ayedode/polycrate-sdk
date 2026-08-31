from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
