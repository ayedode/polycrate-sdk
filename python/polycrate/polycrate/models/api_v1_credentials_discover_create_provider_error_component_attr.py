from typing import Literal

ApiV1CredentialsDiscoverCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CREDENTIALS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_credentials_discover_create_provider_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateProviderErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
