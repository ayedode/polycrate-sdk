from typing import Literal

ApiV1EndpointsReconcileCreateRegionErrorComponentAttr = Literal["region"]

API_V1_ENDPOINTS_RECONCILE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_endpoints_reconcile_create_region_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateRegionErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
