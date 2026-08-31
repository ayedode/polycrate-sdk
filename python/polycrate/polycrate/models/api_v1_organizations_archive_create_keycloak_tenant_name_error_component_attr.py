from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponentAttr = Literal["keycloak_tenant_name"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponentAttr
] = {
    "keycloak_tenant_name",
}


def check_api_v1_organizations_archive_create_keycloak_tenant_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
