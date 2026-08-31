from typing import Literal

ApiV1OrganizationsIconUploadCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_organizations_icon_upload_create_scope_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateScopeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
