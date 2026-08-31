from typing import Literal

ApiV1WorkspacesReconcileCreateKindErrorComponentAttr = Literal["kind"]

API_V1_WORKSPACES_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_workspaces_reconcile_create_kind_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateKindErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
