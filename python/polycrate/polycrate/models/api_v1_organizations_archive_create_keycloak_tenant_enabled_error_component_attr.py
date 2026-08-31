from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponentAttr = Literal["keycloak_tenant_enabled"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponentAttr
] = {
    "keycloak_tenant_enabled",
}


def check_api_v1_organizations_archive_create_keycloak_tenant_enabled_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
