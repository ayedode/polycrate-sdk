from typing import Literal

ApiV1OrganizationsDiscoverCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_organizations_discover_create_provider_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateProviderErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
