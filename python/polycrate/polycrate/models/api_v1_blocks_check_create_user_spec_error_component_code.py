from typing import Literal

ApiV1BlocksCheckCreateUserSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_CHECK_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateUserSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_check_create_user_spec_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateUserSpecErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
