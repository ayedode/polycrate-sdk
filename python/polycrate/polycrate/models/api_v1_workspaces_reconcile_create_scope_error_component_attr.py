from typing import Literal

ApiV1WorkspacesReconcileCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_WORKSPACES_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_workspaces_reconcile_create_scope_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateScopeErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
