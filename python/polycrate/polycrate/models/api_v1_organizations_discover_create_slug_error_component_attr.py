from typing import Literal

ApiV1OrganizationsDiscoverCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_organizations_discover_create_slug_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateSlugErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
