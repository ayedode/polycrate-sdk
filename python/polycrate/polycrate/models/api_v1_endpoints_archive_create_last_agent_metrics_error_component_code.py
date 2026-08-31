from typing import Literal

ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_archive_create_last_agent_metrics_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
