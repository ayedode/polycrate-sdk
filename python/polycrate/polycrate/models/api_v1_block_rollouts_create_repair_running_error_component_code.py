from typing import Literal

ApiV1BlockRolloutsCreateRepairRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateRepairRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_create_repair_running_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateRepairRunningErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
