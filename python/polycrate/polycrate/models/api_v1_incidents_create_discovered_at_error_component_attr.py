from typing import Literal

ApiV1IncidentsCreateDiscoveredAtErrorComponentAttr = Literal["discovered_at"]

API_V1_INCIDENTS_CREATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateDiscoveredAtErrorComponentAttr
] = {
    "discovered_at",
}


def check_api_v1_incidents_create_discovered_at_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateDiscoveredAtErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_DISCOVERED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
