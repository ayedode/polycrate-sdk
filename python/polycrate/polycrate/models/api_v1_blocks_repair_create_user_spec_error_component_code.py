from typing import Literal

ApiV1BlocksRepairCreateUserSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_REPAIR_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateUserSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_repair_create_user_spec_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateUserSpecErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
