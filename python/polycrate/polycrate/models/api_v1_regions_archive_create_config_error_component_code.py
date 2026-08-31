from typing import Literal

ApiV1RegionsArchiveCreateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsArchiveCreateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_archive_create_config_error_component_code(
    value: str,
) -> ApiV1RegionsArchiveCreateConfigErrorComponentCode:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
