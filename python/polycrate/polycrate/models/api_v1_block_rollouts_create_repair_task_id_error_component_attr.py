from typing import Literal

ApiV1BlockRolloutsCreateRepairTaskIdErrorComponentAttr = Literal["repair_task_id"]

API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateRepairTaskIdErrorComponentAttr
] = {
    "repair_task_id",
}


def check_api_v1_block_rollouts_create_repair_task_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateRepairTaskIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
