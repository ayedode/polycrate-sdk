from typing import Literal

ApiV1EndpointsReconcileCreatePopEndpointErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_RECONCILE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreatePopEndpointErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_reconcile_create_pop_endpoint_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreatePopEndpointErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
