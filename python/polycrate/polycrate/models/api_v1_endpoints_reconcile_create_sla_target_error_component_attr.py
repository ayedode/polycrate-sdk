from typing import Literal

ApiV1EndpointsReconcileCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ENDPOINTS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_endpoints_reconcile_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateSlaTargetErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
