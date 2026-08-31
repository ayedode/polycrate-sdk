from typing import Literal

ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_organizations_icon_upload_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
