from typing import Literal

ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponentAttr = Literal["last_agent_metrics"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponentAttr
] = {
    "last_agent_metrics",
}


def check_api_v1_endpoints_archive_create_last_agent_metrics_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
