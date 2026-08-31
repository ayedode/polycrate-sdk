from typing import Literal

ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_partial_update_discovery_running_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
