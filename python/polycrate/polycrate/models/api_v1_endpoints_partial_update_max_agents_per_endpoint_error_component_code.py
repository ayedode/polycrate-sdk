from typing import Literal

ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ENDPOINTS_PARTIAL_UPDATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_partial_update_max_agents_per_endpoint_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
