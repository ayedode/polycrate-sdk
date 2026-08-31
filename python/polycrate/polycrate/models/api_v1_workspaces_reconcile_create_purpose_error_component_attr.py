from typing import Literal

ApiV1WorkspacesReconcileCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_RECONCILE_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_reconcile_create_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
