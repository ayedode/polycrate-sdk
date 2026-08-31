from typing import Literal

ApiV1WorkspacesReconcileCreatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_RECONCILE_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_reconcile_create_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
