from typing import Literal

ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_ARCHIVE_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_archive_create_discovery_running_error_component_code(
    value: str,
) -> ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponentCode:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
