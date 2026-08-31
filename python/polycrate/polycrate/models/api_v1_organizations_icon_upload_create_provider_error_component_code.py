from typing import Literal

ApiV1OrganizationsIconUploadCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_icon_upload_create_provider_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateProviderErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
