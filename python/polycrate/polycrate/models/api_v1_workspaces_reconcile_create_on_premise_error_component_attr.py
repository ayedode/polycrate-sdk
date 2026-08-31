from typing import Literal

ApiV1WorkspacesReconcileCreateOnPremiseErrorComponentAttr = Literal["on_premise"]

API_V1_WORKSPACES_RECONCILE_CREATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateOnPremiseErrorComponentAttr
] = {
    "on_premise",
}


def check_api_v1_workspaces_reconcile_create_on_premise_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateOnPremiseErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
