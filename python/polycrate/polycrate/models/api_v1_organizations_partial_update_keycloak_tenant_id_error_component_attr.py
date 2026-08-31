from typing import Literal

ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponentAttr = Literal["keycloak_tenant_id"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponentAttr
] = {
    "keycloak_tenant_id",
}


def check_api_v1_organizations_partial_update_keycloak_tenant_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KEYCLOAK_TENANT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
