from typing import Literal

ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_organizations_icon_upload_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
