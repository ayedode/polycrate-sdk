from typing import Literal

ApiV1OrganizationsDiscoverCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_discover_create_provider_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateProviderErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
