from typing import Literal

ApiV1BlockRolloutsUpdateRepairRunningErrorComponentAttr = Literal["repair_running"]

API_V1_BLOCK_ROLLOUTS_UPDATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateRepairRunningErrorComponentAttr
] = {
    "repair_running",
}


def check_api_v1_block_rollouts_update_repair_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateRepairRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
