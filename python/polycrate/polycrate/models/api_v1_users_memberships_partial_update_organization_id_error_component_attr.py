from typing import Literal

ApiV1UsersMembershipsPartialUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1UsersMembershipsPartialUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_users_memberships_partial_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1UsersMembershipsPartialUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
