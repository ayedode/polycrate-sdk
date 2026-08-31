from typing import Literal

ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_icon_upload_create_keycloak_role_group_ids_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
