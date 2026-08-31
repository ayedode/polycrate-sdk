from typing import Literal

ApiV1BlocksRepairCreateActionsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_REPAIR_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateActionsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_repair_create_actions_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateActionsErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
