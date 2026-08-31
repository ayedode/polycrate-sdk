from typing import Literal

ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_discover_create_provider_image_os_version_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
