from typing import Literal

ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_CREDENTIALS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_credentials_discover_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
