from typing import Literal

ApiV1EndpointsReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ENDPOINTS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_endpoints_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
