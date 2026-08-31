from typing import Literal

ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponentAttr = Literal["workspace_default_owner_id"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponentAttr
] = {
    "workspace_default_owner_id",
}


def check_api_v1_organizations_reconcile_create_workspace_default_owner_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
