from typing import Literal

ApiV1RegionsUpdateReconciliationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsUpdateReconciliationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_update_reconciliation_running_error_component_code(
    value: str,
) -> ApiV1RegionsUpdateReconciliationRunningErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
