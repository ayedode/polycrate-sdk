from typing import Literal

ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponentAttr = Literal["provider_image_os_architecture"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponentAttr
] = {
    "provider_image_os_architecture",
}


def check_api_v1_hosts_partial_update_provider_image_os_architecture_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
