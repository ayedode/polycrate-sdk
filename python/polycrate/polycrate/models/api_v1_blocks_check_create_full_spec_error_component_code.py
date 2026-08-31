from typing import Literal

ApiV1BlocksCheckCreateFullSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_CHECK_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateFullSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_check_create_full_spec_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateFullSpecErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
