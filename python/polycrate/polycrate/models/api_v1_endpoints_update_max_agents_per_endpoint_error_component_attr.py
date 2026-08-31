from typing import Literal

ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponentAttr = Literal["max_agents_per_endpoint"]

API_V1_ENDPOINTS_UPDATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponentAttr
] = {
    "max_agents_per_endpoint",
}


def check_api_v1_endpoints_update_max_agents_per_endpoint_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateMaxAgentsPerEndpointErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
