from typing import Literal

ApiV1HostsReconcileCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_HOSTS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_hosts_reconcile_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateSloTargetErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
