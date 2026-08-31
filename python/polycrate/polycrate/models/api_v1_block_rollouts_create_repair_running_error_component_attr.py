from typing import Literal

ApiV1BlockRolloutsCreateRepairRunningErrorComponentAttr = Literal["repair_running"]

API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateRepairRunningErrorComponentAttr
] = {
    "repair_running",
}


def check_api_v1_block_rollouts_create_repair_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateRepairRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
