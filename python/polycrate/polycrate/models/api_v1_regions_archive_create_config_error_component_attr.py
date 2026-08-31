from typing import Literal

ApiV1RegionsArchiveCreateConfigErrorComponentAttr = Literal["config"]

API_V1_REGIONS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_regions_archive_create_config_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateConfigErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
