from typing import Literal

ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponentAttr = Literal["last_agent_metrics"]

API_V1_ENDPOINTS_RECONCILE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponentAttr
] = {
    "last_agent_metrics",
}


def check_api_v1_endpoints_reconcile_create_last_agent_metrics_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_LAST_AGENT_METRICS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
