from typing import Literal

ApiV1BlocksCheckCreateIsBehindStableErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CHECK_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateIsBehindStableErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_check_create_is_behind_stable_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateIsBehindStableErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
