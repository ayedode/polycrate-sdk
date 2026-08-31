from typing import Literal

ApiV1EndpointsReconcileCreateSpecErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_RECONCILE_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_reconcile_create_spec_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateSpecErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
