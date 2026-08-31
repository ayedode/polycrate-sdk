from typing import Literal

ApiV1BlocksCreateIsBehindStableErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCreateIsBehindStableErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_create_is_behind_stable_error_component_code(
    value: str,
) -> ApiV1BlocksCreateIsBehindStableErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
