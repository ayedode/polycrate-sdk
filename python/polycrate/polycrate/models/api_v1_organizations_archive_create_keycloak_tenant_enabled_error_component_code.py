from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_archive_create_keycloak_tenant_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
