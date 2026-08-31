from typing import Literal

ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_RECONCILE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_reconcile_create_loadbalancer_instance_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
