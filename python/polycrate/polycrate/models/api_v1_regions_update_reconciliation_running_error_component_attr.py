from typing import Literal

ApiV1RegionsUpdateReconciliationRunningErrorComponentAttr = Literal["reconciliation_running"]

API_V1_REGIONS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsUpdateReconciliationRunningErrorComponentAttr
] = {
    "reconciliation_running",
}


def check_api_v1_regions_update_reconciliation_running_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateReconciliationRunningErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
