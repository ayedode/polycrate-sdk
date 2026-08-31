from typing import Literal

ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_discover_create_keycloak_tenant_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
