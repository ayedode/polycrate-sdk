from typing import Literal

ApiV1BlocksArchiveCreateChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_ARCHIVE_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateChecksumErrorComponentAttr
] = {
    "checksum",
}


def check_api_v1_blocks_archive_create_checksum_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
