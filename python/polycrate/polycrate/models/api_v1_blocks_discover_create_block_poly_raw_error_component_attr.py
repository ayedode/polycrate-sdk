from typing import Literal

ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponentAttr = Literal["block_poly_raw"]

API_V1_BLOCKS_DISCOVER_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponentAttr
] = {
    "block_poly_raw",
}


def check_api_v1_blocks_discover_create_block_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
