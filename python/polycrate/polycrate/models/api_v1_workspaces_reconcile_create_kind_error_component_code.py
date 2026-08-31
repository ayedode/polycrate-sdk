from typing import Literal

ApiV1WorkspacesReconcileCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_reconcile_create_kind_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreateKindErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
