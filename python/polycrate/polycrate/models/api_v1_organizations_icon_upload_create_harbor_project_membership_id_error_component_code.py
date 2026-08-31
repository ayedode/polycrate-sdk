from typing import Literal

ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_icon_upload_create_harbor_project_membership_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_HARBOR_PROJECT_MEMBERSHIP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
