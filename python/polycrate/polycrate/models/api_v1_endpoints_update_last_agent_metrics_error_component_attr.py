from typing import Literal

ApiV1EndpointsUpdateLastAgentMetricsErrorComponentAttr = Literal["last_agent_metrics"]

API_V1_ENDPOINTS_UPDATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateLastAgentMetricsErrorComponentAttr
] = {
    "last_agent_metrics",
}


def check_api_v1_endpoints_update_last_agent_metrics_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateLastAgentMetricsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
