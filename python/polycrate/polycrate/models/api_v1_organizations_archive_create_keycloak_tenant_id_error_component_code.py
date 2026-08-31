from typing import Literal

ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_archive_create_keycloak_tenant_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
