from typing import Literal

ApiV1WorkspacesReconcileCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_RECONCILE_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_reconcile_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
