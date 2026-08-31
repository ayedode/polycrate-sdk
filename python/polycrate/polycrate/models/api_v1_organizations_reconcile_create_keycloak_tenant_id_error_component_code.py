from typing import Literal

ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_reconcile_create_keycloak_tenant_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
