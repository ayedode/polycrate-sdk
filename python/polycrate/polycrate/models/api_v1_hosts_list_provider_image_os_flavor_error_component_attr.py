from typing import Literal

ApiV1HostsListProviderImageOsFlavorErrorComponentAttr = Literal["provider_image_os_flavor"]

API_V1_HOSTS_LIST_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsListProviderImageOsFlavorErrorComponentAttr
] = {
    "provider_image_os_flavor",
}


def check_api_v1_hosts_list_provider_image_os_flavor_error_component_attr(
    value: str,
) -> ApiV1HostsListProviderImageOsFlavorErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
