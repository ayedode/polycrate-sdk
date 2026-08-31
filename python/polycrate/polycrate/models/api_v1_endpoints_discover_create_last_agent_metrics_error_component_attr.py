from typing import Literal

ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponentAttr = Literal["last_agent_metrics"]

API_V1_ENDPOINTS_DISCOVER_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponentAttr
] = {
    "last_agent_metrics",
}


def check_api_v1_endpoints_discover_create_last_agent_metrics_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
