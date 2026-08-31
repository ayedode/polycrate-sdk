from typing import Literal

ApiV1BlocksDiscoverCreateFromBlockErrorComponentAttr = Literal["from_block"]

API_V1_BLOCKS_DISCOVER_CREATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateFromBlockErrorComponentAttr
] = {
    "from_block",
}


def check_api_v1_blocks_discover_create_from_block_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateFromBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
