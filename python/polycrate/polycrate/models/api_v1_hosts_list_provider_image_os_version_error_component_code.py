from typing import Literal

ApiV1HostsListProviderImageOsVersionErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_HOSTS_LIST_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsListProviderImageOsVersionErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_hosts_list_provider_image_os_version_error_component_code(
    value: str,
) -> ApiV1HostsListProviderImageOsVersionErrorComponentCode:
    if value in API_V1_HOSTS_LIST_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
