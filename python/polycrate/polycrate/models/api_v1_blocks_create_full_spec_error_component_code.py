from typing import Literal

ApiV1BlocksCreateFullSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateFullSpecErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_create_full_spec_error_component_code(
    value: str,
) -> ApiV1BlocksCreateFullSpecErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
