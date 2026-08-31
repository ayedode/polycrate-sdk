from typing import Literal

ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponentAttr = Literal["discovered_at"]

API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponentAttr
] = {
    "discovered_at",
}


def check_api_v1_incidents_partial_update_discovered_at_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
