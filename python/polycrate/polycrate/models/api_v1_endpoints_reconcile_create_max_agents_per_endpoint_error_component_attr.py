from typing import Literal

ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponentAttr = Literal["max_agents_per_endpoint"]

API_V1_ENDPOINTS_RECONCILE_CREATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponentAttr
] = {
    "max_agents_per_endpoint",
}


def check_api_v1_endpoints_reconcile_create_max_agents_per_endpoint_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_MAX_AGENTS_PER_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
