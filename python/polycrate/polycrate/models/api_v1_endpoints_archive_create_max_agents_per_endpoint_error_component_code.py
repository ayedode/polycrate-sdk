from typing import Literal

ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ENDPOINTS_ARCHIVE_CREATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_archive_create_max_agents_per_endpoint_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
