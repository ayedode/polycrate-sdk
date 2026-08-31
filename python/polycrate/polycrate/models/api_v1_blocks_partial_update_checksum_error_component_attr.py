from typing import Literal

ApiV1BlocksPartialUpdateChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_PARTIAL_UPDATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateChecksumErrorComponentAttr
] = {
    "checksum",
}


def check_api_v1_blocks_partial_update_checksum_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
