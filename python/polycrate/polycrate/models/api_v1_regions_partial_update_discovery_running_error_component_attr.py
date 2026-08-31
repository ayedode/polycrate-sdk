from typing import Literal

ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponentAttr = Literal["discovery_running"]

API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponentAttr
] = {
    "discovery_running",
}


def check_api_v1_regions_partial_update_discovery_running_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
