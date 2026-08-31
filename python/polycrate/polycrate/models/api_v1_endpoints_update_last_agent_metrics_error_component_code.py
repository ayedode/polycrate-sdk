from typing import Literal

ApiV1EndpointsUpdateLastAgentMetricsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_UPDATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateLastAgentMetricsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_update_last_agent_metrics_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateLastAgentMetricsErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
