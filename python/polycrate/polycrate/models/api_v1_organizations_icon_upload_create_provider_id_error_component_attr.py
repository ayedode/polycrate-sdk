from typing import Literal

ApiV1OrganizationsIconUploadCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_organizations_icon_upload_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateProviderIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
