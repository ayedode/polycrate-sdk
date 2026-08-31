from typing import Literal

ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponentAttr = Literal["harbor_project_membership_id"]

API_V1_ORGANIZATIONS_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponentAttr
] = {
    "harbor_project_membership_id",
}


def check_api_v1_organizations_create_harbor_project_membership_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
