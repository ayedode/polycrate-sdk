from typing import Literal

ApiV1IncidentsCreateDiscoveredAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_INCIDENTS_CREATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreateDiscoveredAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_incidents_create_discovered_at_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateDiscoveredAtErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_DISCOVERED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
