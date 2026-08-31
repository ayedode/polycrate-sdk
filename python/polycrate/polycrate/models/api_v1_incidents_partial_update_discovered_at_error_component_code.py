from typing import Literal

ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_incidents_partial_update_discovered_at_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
