from typing import Literal

ApiV1PopsReconcileCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_POPS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pops_reconcile_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateSloTargetErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
