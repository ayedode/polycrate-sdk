from typing import Literal

ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponentAttr = Literal["provider_image_os_flavor"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponentAttr
] = {
    "provider_image_os_flavor",
}


def check_api_v1_hosts_reconcile_create_provider_image_os_flavor_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_OS_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
