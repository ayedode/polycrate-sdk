from typing import Literal

ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_partial_update_keycloak_role_group_ids_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
