from typing import Literal

ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponentAttr = Literal["keycloak_tenant_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponentAttr
] = {
    "keycloak_tenant_id",
}


def check_api_v1_organizations_discover_create_keycloak_tenant_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
