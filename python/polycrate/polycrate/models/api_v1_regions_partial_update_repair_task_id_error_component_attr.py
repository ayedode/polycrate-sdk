from typing import Literal

ApiV1RegionsPartialUpdateRepairTaskIdErrorComponentAttr = Literal["repair_task_id"]

API_V1_REGIONS_PARTIAL_UPDATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateRepairTaskIdErrorComponentAttr
] = {
    "repair_task_id",
}


def check_api_v1_regions_partial_update_repair_task_id_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateRepairTaskIdErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
