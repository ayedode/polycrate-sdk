from typing import Literal

ApiV1WorkspacesReconcileCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_WORKSPACES_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_workspaces_reconcile_create_archived_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateArchivedErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
