from typing import Literal

ApiV1OrganizationsIconUploadCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1_organizations_icon_upload_create_alias_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateAliasErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
