from typing import Literal

ApiV1EndpointsCreateLastAgentMetricsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateLastAgentMetricsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_create_last_agent_metrics_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateLastAgentMetricsErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
