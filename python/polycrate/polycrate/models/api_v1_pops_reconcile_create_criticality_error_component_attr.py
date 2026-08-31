from typing import Literal

ApiV1PopsReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_POPS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pops_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
