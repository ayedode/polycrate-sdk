from typing import Literal

ApiV1OrganizationsDiscoverCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_organizations_discover_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateProviderIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
