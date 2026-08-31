from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponentAttr = Literal["keycloak_tenant_id"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponentAttr
] = {
    "keycloak_tenant_id",
}


def check_api_v1_organizations_archive_create_keycloak_tenant_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
