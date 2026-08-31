from typing import Literal

ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponentAttr = Literal["keycloak_tenant_name"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponentAttr
] = {
    "keycloak_tenant_name",
}


def check_api_v1_organizations_discover_create_keycloak_tenant_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
