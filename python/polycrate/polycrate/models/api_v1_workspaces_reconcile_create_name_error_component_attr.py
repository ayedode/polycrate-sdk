from typing import Literal

ApiV1WorkspacesReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_workspaces_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
