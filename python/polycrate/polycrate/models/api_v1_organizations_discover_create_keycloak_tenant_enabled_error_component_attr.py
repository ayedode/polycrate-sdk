from typing import Literal

ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponentAttr = Literal["keycloak_tenant_enabled"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponentAttr
] = {
    "keycloak_tenant_enabled",
}


def check_api_v1_organizations_discover_create_keycloak_tenant_enabled_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
