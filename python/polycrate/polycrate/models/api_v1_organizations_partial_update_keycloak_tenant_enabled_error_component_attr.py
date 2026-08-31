from typing import Literal

ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponentAttr = Literal["keycloak_tenant_enabled"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponentAttr
] = {
    "keycloak_tenant_enabled",
}


def check_api_v1_organizations_partial_update_keycloak_tenant_enabled_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
