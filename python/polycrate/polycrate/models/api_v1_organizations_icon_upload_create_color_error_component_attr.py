from typing import Literal

ApiV1OrganizationsIconUploadCreateColorErrorComponentAttr = Literal["color"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateColorErrorComponentAttr
] = {
    "color",
}


def check_api_v1_organizations_icon_upload_create_color_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateColorErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
