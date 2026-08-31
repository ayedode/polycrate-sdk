from typing import Literal

ApiV1BlocksArchiveCreateBlockPolyRawErrorComponentAttr = Literal["block_poly_raw"]

API_V1_BLOCKS_ARCHIVE_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateBlockPolyRawErrorComponentAttr
] = {
    "block_poly_raw",
}


def check_api_v1_blocks_archive_create_block_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateBlockPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_BLOCK_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
