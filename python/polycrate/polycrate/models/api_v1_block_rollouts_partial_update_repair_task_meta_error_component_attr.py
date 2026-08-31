from typing import Literal

ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponentAttr = Literal["repair_task_meta"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponentAttr
] = {
    "repair_task_meta",
}


def check_api_v1_block_rollouts_partial_update_repair_task_meta_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
