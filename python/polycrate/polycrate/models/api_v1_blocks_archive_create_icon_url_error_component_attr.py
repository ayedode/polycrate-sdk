from typing import Literal

ApiV1BlocksArchiveCreateIconUrlErrorComponentAttr = Literal["icon_url"]

API_V1_BLOCKS_ARCHIVE_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateIconUrlErrorComponentAttr
] = {
    "icon_url",
}


def check_api_v1_blocks_archive_create_icon_url_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateIconUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
