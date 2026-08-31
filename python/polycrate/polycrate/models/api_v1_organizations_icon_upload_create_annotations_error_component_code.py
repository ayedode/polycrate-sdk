from typing import Literal

ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_icon_upload_create_annotations_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
