from typing import Literal

ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponentAttr = Literal["loadbalancer_instance"]

API_V1_ENDPOINTS_RECONCILE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponentAttr
] = {
    "loadbalancer_instance",
}


def check_api_v1_endpoints_reconcile_create_loadbalancer_instance_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
