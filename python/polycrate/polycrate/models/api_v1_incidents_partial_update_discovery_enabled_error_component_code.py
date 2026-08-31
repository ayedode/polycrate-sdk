from typing import Literal

ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_partial_update_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
