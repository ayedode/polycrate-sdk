from typing import Literal

ApiV1EndpointsReconcileCreatePopEndpointErrorComponentAttr = Literal["pop_endpoint"]

API_V1_ENDPOINTS_RECONCILE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreatePopEndpointErrorComponentAttr
] = {
    "pop_endpoint",
}


def check_api_v1_endpoints_reconcile_create_pop_endpoint_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreatePopEndpointErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
