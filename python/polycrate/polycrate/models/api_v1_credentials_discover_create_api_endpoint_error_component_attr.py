from typing import Literal

ApiV1CredentialsDiscoverCreateApiEndpointErrorComponentAttr = Literal["api_endpoint"]

API_V1_CREDENTIALS_DISCOVER_CREATE_API_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateApiEndpointErrorComponentAttr
] = {
    "api_endpoint",
}


def check_api_v1_credentials_discover_create_api_endpoint_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateApiEndpointErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_API_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_API_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
