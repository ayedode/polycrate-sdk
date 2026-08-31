from typing import Literal

ApiV1BlocksCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCKS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateScopeErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_blocks_create_scope_error_component_code(value: str) -> ApiV1BlocksCreateScopeErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
