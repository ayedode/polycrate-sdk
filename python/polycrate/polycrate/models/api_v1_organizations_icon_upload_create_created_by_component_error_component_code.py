from typing import Literal

ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_icon_upload_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
