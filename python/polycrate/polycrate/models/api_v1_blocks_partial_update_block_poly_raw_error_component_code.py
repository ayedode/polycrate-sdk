from typing import Literal

ApiV1BlocksPartialUpdateBlockPolyRawErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_PARTIAL_UPDATE_BLOCK_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateBlockPolyRawErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_partial_update_block_poly_raw_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateBlockPolyRawErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_BLOCK_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_BLOCK_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
