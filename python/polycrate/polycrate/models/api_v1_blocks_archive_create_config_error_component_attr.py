from typing import Literal

ApiV1BlocksArchiveCreateConfigErrorComponentAttr = Literal["config"]

API_V1_BLOCKS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_blocks_archive_create_config_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateConfigErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
