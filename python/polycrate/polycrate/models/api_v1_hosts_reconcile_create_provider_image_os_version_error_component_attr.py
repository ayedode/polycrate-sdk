from typing import Literal

ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponentAttr = Literal["provider_image_os_version"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponentAttr
] = {
    "provider_image_os_version",
}


def check_api_v1_hosts_reconcile_create_provider_image_os_version_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_OS_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
