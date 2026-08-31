from typing import Literal

ApiV1BlocksDiscoverCreateIsBehindStableErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_DISCOVER_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateIsBehindStableErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_discover_create_is_behind_stable_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateIsBehindStableErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
