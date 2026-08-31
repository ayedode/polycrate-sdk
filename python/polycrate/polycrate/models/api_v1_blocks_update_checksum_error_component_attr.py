from typing import Literal

ApiV1BlocksUpdateChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_UPDATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateChecksumErrorComponentAttr] = {
    "checksum",
}


def check_api_v1_blocks_update_checksum_error_component_attr(value: str) -> ApiV1BlocksUpdateChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
