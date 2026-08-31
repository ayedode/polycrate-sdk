from typing import Literal

ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_reconcile_create_keycloak_role_group_ids_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_ROLE_GROUP_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
