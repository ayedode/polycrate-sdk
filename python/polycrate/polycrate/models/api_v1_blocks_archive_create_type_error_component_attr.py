from typing import Literal

ApiV1BlocksArchiveCreateTypeErrorComponentAttr = Literal["type"]

API_V1_BLOCKS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksArchiveCreateTypeErrorComponentAttr] = {
    "type",
}


def check_api_v1_blocks_archive_create_type_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateTypeErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
