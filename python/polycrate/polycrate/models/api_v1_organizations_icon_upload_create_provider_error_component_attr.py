from typing import Literal

ApiV1OrganizationsIconUploadCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_organizations_icon_upload_create_provider_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateProviderErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
