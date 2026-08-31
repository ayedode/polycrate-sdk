from typing import Literal

ApiV1BlocksDiscoverCreateIsBehindStableErrorComponentAttr = Literal["is_behind_stable"]

API_V1_BLOCKS_DISCOVER_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateIsBehindStableErrorComponentAttr
] = {
    "is_behind_stable",
}


def check_api_v1_blocks_discover_create_is_behind_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateIsBehindStableErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
