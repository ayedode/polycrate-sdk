from typing import Literal

ApiV1HostsReconcileCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_HOSTS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_hosts_reconcile_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateSlaTargetErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
