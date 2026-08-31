from typing import Literal

ApiV1WorkspacesReconcileCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_reconcile_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
