from typing import Literal

ApiV1OrganizationsDiscoverCreateColorErrorComponentAttr = Literal["color"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateColorErrorComponentAttr
] = {
    "color",
}


def check_api_v1_organizations_discover_create_color_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateColorErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
