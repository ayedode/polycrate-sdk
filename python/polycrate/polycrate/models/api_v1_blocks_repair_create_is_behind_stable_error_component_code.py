from typing import Literal

ApiV1BlocksRepairCreateIsBehindStableErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_REPAIR_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateIsBehindStableErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_repair_create_is_behind_stable_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateIsBehindStableErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
