from typing import Literal

ApiV1UsersMembershipsPartialUpdateOrganizationIdErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1UsersMembershipsPartialUpdateOrganizationIdErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_users_memberships_partial_update_organization_id_error_component_code(
    value: str,
) -> ApiV1UsersMembershipsPartialUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
