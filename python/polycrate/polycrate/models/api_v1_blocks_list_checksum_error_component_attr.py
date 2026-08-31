from typing import Literal

ApiV1BlocksListChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_LIST_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksListChecksumErrorComponentAttr] = {
    "checksum",
}


def check_api_v1_blocks_list_checksum_error_component_attr(value: str) -> ApiV1BlocksListChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
