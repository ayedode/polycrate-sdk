from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponentAttr = Literal["keycloak_role_group_ids"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponentAttr
] = {
    "keycloak_role_group_ids",
}


def check_api_v1_organizations_archive_create_keycloak_role_group_ids_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
