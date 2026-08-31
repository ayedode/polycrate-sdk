from typing import Literal

ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponentAttr = Literal["harbor_project_membership_id"]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponentAttr
] = {
    "harbor_project_membership_id",
}


def check_api_v1_organizations_update_harbor_project_membership_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
