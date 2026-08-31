from typing import Literal

ApiV1HostsReconcileCreateProviderImageErrorComponentAttr = Literal["provider_image"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateProviderImageErrorComponentAttr
] = {
    "provider_image",
}


def check_api_v1_hosts_reconcile_create_provider_image_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateProviderImageErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_IMAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
