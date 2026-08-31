from typing import Literal

ApiV1PopsReconcileCreateRegionErrorComponentAttr = Literal["region"]

API_V1_POPS_RECONCILE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_pops_reconcile_create_region_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateRegionErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
