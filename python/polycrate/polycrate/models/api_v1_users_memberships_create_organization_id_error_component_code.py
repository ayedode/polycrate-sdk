from typing import Literal

ApiV1UsersMembershipsCreateOrganizationIdErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_USERS_MEMBERSHIPS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1UsersMembershipsCreateOrganizationIdErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_users_memberships_create_organization_id_error_component_code(
    value: str,
) -> ApiV1UsersMembershipsCreateOrganizationIdErrorComponentCode:
    if value in API_V1_USERS_MEMBERSHIPS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
