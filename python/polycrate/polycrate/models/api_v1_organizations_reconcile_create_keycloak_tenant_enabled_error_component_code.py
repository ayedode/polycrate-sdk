from typing import Literal

ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_reconcile_create_keycloak_tenant_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
