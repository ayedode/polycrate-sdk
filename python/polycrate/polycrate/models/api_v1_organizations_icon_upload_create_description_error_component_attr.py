from typing import Literal

ApiV1OrganizationsIconUploadCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_organizations_icon_upload_create_description_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateDescriptionErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
