from typing import Literal

ApiV1WorkspacesReconcileCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_WORKSPACES_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_workspaces_reconcile_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateSlaTargetErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
