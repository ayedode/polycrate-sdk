from typing import Literal

ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponentAttr = Literal["harbor_project_membership_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponentAttr
] = {
    "harbor_project_membership_id",
}


def check_api_v1_organizations_discover_create_harbor_project_membership_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
