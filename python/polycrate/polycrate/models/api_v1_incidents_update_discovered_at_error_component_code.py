from typing import Literal

ApiV1IncidentsUpdateDiscoveredAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_INCIDENTS_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateDiscoveredAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_incidents_update_discovered_at_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateDiscoveredAtErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
