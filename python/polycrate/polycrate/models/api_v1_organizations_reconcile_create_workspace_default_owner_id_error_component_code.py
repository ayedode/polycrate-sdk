from typing import Literal

ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_organizations_reconcile_create_workspace_default_owner_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
