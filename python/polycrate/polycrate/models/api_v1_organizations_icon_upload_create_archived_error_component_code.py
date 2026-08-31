from typing import Literal

ApiV1OrganizationsIconUploadCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_icon_upload_create_archived_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateArchivedErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
