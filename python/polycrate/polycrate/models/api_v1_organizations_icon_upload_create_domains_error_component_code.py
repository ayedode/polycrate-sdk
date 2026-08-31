from typing import Literal

ApiV1OrganizationsIconUploadCreateDomainsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateDomainsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_icon_upload_create_domains_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateDomainsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
