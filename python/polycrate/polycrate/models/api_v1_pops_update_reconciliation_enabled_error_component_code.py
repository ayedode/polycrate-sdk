from typing import Literal

ApiV1PopsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_POPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pops_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PopsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_POPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
