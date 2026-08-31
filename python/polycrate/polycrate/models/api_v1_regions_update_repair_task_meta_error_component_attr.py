from typing import Literal

ApiV1RegionsUpdateRepairTaskMetaErrorComponentAttr = Literal["repair_task_meta"]

API_V1_REGIONS_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsUpdateRepairTaskMetaErrorComponentAttr
] = {
    "repair_task_meta",
}


def check_api_v1_regions_update_repair_task_meta_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateRepairTaskMetaErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
