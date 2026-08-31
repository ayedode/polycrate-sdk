from typing import Literal

ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_REGIONS_PARTIAL_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_regions_partial_update_repair_task_meta_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
