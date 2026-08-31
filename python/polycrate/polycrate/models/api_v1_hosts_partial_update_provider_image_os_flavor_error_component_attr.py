from typing import Literal

ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponentAttr = Literal["provider_image_os_flavor"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponentAttr
] = {
    "provider_image_os_flavor",
}


def check_api_v1_hosts_partial_update_provider_image_os_flavor_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
