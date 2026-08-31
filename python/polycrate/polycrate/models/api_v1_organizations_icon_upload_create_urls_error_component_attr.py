from typing import Literal

ApiV1OrganizationsIconUploadCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_organizations_icon_upload_create_urls_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateUrlsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
