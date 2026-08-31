from typing import Literal

ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_DISCOVER_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_discover_create_block_poly_raw_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
