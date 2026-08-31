from typing import Literal

ApiV1PopsReconcileCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_POPS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pops_reconcile_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateTolerationsErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
