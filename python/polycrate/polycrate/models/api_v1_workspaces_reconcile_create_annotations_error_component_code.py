from typing import Literal

ApiV1WorkspacesReconcileCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_WORKSPACES_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_workspaces_reconcile_create_annotations_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreateAnnotationsErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
