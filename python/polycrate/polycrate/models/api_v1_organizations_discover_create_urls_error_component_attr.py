from typing import Literal

ApiV1OrganizationsDiscoverCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_organizations_discover_create_urls_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateUrlsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
