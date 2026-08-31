from typing import Literal

ApiV1BlocksCheckCreateChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_CHECK_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateChecksumErrorComponentAttr
] = {
    "checksum",
}


def check_api_v1_blocks_check_create_checksum_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
