from typing import Literal

ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponentAttr = Literal["icon_content_type"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponentAttr
] = {
    "icon_content_type",
}


def check_api_v1_organizations_discover_create_icon_content_type_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
