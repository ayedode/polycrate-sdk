from typing import Literal

ApiV1BlocksPartialUpdateIsBehindStableErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_PARTIAL_UPDATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateIsBehindStableErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_partial_update_is_behind_stable_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateIsBehindStableErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
