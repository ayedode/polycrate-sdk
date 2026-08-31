from typing import Literal

ApiV1BlocksRepairCreateFullSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_REPAIR_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateFullSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_repair_create_full_spec_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateFullSpecErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
