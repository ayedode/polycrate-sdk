from typing import Literal

ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponentAttr = Literal["keycloak_role_group_ids"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponentAttr
] = {
    "keycloak_role_group_ids",
}


def check_api_v1_organizations_icon_upload_create_keycloak_role_group_ids_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
