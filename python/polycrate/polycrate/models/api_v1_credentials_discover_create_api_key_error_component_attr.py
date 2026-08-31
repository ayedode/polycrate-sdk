from typing import Literal

ApiV1CredentialsDiscoverCreateApiKeyErrorComponentAttr = Literal["api_key"]

API_V1_CREDENTIALS_DISCOVER_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateApiKeyErrorComponentAttr
] = {
    "api_key",
}


def check_api_v1_credentials_discover_create_api_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateApiKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
