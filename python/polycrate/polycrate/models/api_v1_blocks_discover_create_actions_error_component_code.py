from typing import Literal

ApiV1BlocksDiscoverCreateActionsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_DISCOVER_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateActionsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_discover_create_actions_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateActionsErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
