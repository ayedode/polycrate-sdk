from typing import Literal

ApiV1IncidentsUpdateDiscoveredAtErrorComponentAttr = Literal["discovered_at"]

API_V1_INCIDENTS_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateDiscoveredAtErrorComponentAttr
] = {
    "discovered_at",
}


def check_api_v1_incidents_update_discovered_at_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateDiscoveredAtErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
