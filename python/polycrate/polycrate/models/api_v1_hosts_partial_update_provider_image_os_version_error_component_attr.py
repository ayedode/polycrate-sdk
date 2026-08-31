from typing import Literal

ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponentAttr = Literal["provider_image_os_version"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponentAttr
] = {
    "provider_image_os_version",
}


def check_api_v1_hosts_partial_update_provider_image_os_version_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
