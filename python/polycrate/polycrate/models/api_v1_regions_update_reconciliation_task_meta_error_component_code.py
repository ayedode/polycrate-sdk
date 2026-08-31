from typing import Literal

ApiV1RegionsUpdateReconciliationTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_REGIONS_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsUpdateReconciliationTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_regions_update_reconciliation_task_meta_error_component_code(
    value: str,
) -> ApiV1RegionsUpdateReconciliationTaskMetaErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
