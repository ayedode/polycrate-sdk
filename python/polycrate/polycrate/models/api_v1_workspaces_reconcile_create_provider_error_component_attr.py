from typing import Literal

ApiV1WorkspacesReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
