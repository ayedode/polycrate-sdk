from typing import Literal

ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_organizations_icon_upload_create_workspace_default_owner_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_WORKSPACE_DEFAULT_OWNER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
