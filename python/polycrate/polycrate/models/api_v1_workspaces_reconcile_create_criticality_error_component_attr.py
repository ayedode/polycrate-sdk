from typing import Literal

ApiV1WorkspacesReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
