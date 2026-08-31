from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_archive_create_keycloak_role_group_ids_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
